import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server address and port
host = '127.0.0.1'  # localhost
port = 1235

# Bind the socket to the address and port
server_socket.bind((host, port))

# Listen for up to 5 queued connections
server_socket.listen(5)
print(f"Server listening on {host}:{port}...")

# Keep the server running indefinitely
while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connected to client: {client_address}")

    # Receive message from the client (up to 1024 bytes)
    BUF_SIZE = 1024
    data = client_socket.recv(BUF_SIZE)
    if not data:
        # No data received (client closed connection)
        client_socket.close()
        continue

    # Decode and print the received message
    message = data.decode('utf-8')
    print(f"Client sent: {message}")

    # Echo the same message back to the client
    client_socket.send(data)

    # Close the connection with this client
    client_socket.close()

# Note: The server will only stop if interrupted (e.g., Ctrl+C)
server_socket.close()