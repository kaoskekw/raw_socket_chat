import socket
import select


def read_requests(read_clients, all_clients):
    responses = {}

    for sock in read_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except Exception as ex:
            print(ex)
            print(f"Client {sock.fileno()} {sock.getpeername()} disconnected.")
            sock.close()
            all_clients.remove(sock)

    return responses


def write_responses(requests, clients_write, all_clients):
    for sock in clients_write:
        if sock in requests:
            try:
                if requests[sock] == '':
                    raise Exception
                resp = requests[sock].upper()
                print(resp)
                sock.send(resp.encode('utf-8'))
            except Exception as ex:
                print(ex)
                print(f"Client {sock.fileno()} {sock.getpeername()} disconnected.")
                all_clients.remove(sock)
                sock.close()


def main():
    host = '127.0.0.1'
    port = 9090
    all_clients = []

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(10)
        server.settimeout(1)

        while True:
            try:
                conn, addr = server.accept()
            except OSError as err:
                pass
            else:
                print(f"Connection request received from {str(addr)}")
                all_clients.append(conn)
            finally:
                wait = 0
                clients_read = []
                clients_write = []
                try:
                    clients_read, clients_write, _ = select.select(all_clients, all_clients, all_clients, wait)
                except Exception as ex:
                    print(ex)

                requests = read_requests(clients_read, all_clients)
                print(requests)
                if requests:
                    write_responses(requests, clients_write, all_clients)


print('Server started')
main()
