import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 65432))
print("Connected to server...")

while True:
    msg = input("Client: ")
    client_socket.sendall(msg.encode())
    
    data = client_socket.recv(1024)
    print(f"Server: {data.decode()}")
