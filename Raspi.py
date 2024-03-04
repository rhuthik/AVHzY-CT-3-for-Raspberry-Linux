import socket

# Define the port to listen on
PORT = 5000

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', PORT))
server_socket.listen(1)
print("Listening for incoming connections on port", PORT)

# Accept a connection
connection, address = server_socket.accept()
print("Connection from:", address)

try:
    while True:
        data = connection.recv(1024)  # Receive data from the client
        if not data:
            break  # Exit loop if no data is received
        message = data.decode('ascii')
        print("Received:", message)
finally:
    # Close the connection
    connection.close()
