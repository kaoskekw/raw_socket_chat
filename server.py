import socket
from threading import Thread


def up_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9111))
    server.listen(20)
    return server


def listen(conn, client_list):
    while True:
        try:
            message = conn.recv(1024).decode()
        except:
            client_list.remove(conn)
        else:
            broadcast(message, client_list, conn)


def broadcast(message, client_list, conn):
    for client in client_list:
        if client != conn:
            client.send(message.encode())
    print(message)


def main():
    server = up_server()
    client_list = []

    while True:
        conn, addr = server.accept()
        print(f'Received connection from {conn.fileno()} {conn.getpeername()}')
        username = conn.recv(1024).decode()
        client_list.append(conn)

        join_message = "\n" + username + "join the chat."
        broadcast(join_message, client_list, conn)

        thread = Thread(target=listen, args=(conn, client_list,))
        thread.daemon = True
        thread.start()


if __name__ == "__main__":
    main()
