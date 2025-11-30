import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1", 65432))

server_socket.listen(1)
print("Server is listening on port 65432...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")
                                                                           
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"Client: {data.decode()}")
    
    msg = input("Server: ")
    conn.sendall(msg.encode())

conn.close()
