import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's address and port
host = '127.0.0.1'  # localhost
port = 1235

# Connect to the server
client_socket.connect((host, port))
print(f"Connected to server at {host}:{port}")

# Get message from user and send to server
message = input("Enter message to send: ")
client_socket.send(message.encode('utf-8'))

# Receive echoed message from the server (up to 1024 bytes)
BUF_SIZE = 1024
data = client_socket.recv(BUF_SIZE).decode('utf-8')
print(f"Server echoed: {data}")

# Close the connection
client_socket.close()
print("Connection closed.")