import socket

host = '127.0.0.1'
port = 9090


def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        while True:
            message = ''
            while message.strip() == '':
                message = input('Me:')
            if message == 'exit':
                break
            client.send(message.encode('utf-8'))
            data = client.recv(1024).decode('utf-8')


if __name__ == '__main__':
    client()
