import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("127.0.0.1", 65432)

print("UDP Client started...")

while True:
    msg = input("Client: ")
    client_socket.sendto(msg.encode(), server_address)
    
    # Receive response
    data, addr = client_socket.recvfrom(1024)
    print(f"Server {addr}: {data.decode()}")
