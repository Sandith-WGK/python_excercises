import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 12345

server_socket.bind((host,port))

server_socket.listen(5)

print(f'Server is listening on {host}:{port}........')

while True:

    client_socket,client_address = server_socket.accept()
    print(f"Connected to client: {client_address}")

    msg = "Hello from server"

    client_socket.send(msg.encode('utf-8'))

    client_socket.close()

server_socket.close()