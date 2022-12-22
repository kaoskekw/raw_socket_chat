import socket
import threading

HOST = '127.0.0.1'
PORT = 9090
CONNECTIONS = 5


def broadcast(msg, client_list):
    for client in client_list:
        client.send(msg.encode('utf-8'))
    print(msg)


def listen(msg, client_list):
    while True:
        try:
            msg = msg.recv(1024).decode
        except:
            client_list.remove(msg)



def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(CONNECTIONS)

    client_list = []

    while True:
        conn, addr = server.accept()
        username = conn.recv(1024).decode('utf-8')
        client_list.append(conn)

        join_msg = username + 'join the chat'
        broadcast(join_msg, client_list)

        thread = threading.Thread(target=listen, args=(conn, client_list,))
        thread.daemon = True
        thread.start()


if __name__ == "__main__":
    main()
