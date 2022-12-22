import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 9090


def listen(server):
    while True:
        msg = server.recv(1024).decode()
        print(msg)


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((HOST, PORT))

    username = input("Enter your nickname: ")
    server.send(username.encode('utf-8'))
    print(server.recv(1024).decode())

    thread = threading.Thread(target=listen, args=(server,))
    thread.daemon = True
    thread.start()

    while True:
        msg = input()

        if msg == "/disconnect":
            break

        server.send(('> ' + username + ': ' + msg).encode('utf-8'))

    server.close()


if __name__ == "__main__":
    main()
