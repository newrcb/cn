import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(("127.0.0.1", 65432))
print("UDP Server is listening on port 65432...")

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Client {addr}: {data.decode()}")
    
    msg = input("Server: ")
    server_socket.sendto(msg.encode(), addr)


