import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 12345

client_socket.connect((host,port))
print(f"Connected to server at {host}:{port}")

# Receive message from the server (up to 1024 bytes)
BUF_SIZE = 1024
data = client_socket.recv(BUF_SIZE).decode('utf-8')
print(f"Server says: {data}")

# Close the connection
client_socket.close()
print("Connection closed.")
