import socket
from threading import Thread


def listen(server, client):
    while True:
        message = server.recv(1024).decode()
        print('\n' + message + '\n' + client + ':',end='')


def main():
    server = socket.socket()
    server.connect(('127.0.0.1', 9111))

    print("""
             *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *
        |\___/|
        )     (             .              '
       =\     /=
         )===(       *
        /     \\
        |     |
       /       \\
       \       /
_/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
|  |  |  |( (  |  |  |  |  |  |  |  |  |  |
|  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
|  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
KEK_CHAT |  |  |  |  |  |  |  |  |  |  |  |
""")

    client = input("Enter your nickname: ")

    server.send((client.encode()))

    thread = Thread(target=listen, args=(server, client,))
    thread.daemon = True
    thread.start()

    while True:
        message = input(client + ' : ')

        if message == '/exit':
            break

        server.send((client + ' : ' + message).encode())

    server.close()


if __name__ == "__main__":
    main()
