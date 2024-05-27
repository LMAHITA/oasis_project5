import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Client: {message}")
                broadcast(f"Client: {message}", client_socket)
            else:
                remove(client_socket)
                break
        except:
            continue

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)

def remove(connection):
    if connection in clients:
        clients.remove(connection)

def server_send():
    while True:
        message = input()
        broadcast(f"Server: {message}", None)
        print(f"Server: {message}")

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(100)

    clients = []

    print("Server started and listening on port 12345...")

    threading.Thread(target=server_send).start()

    while True:
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        print(f"{client_address} connected")
        threading.Thread(target=handle_client, args=(client_socket,)).start()
