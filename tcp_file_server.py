import socket 
# Server configuration 
HOST = '127.0.0.1'   # Localhost 
PORT = 5001          

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.bind((HOST, PORT)) 
server_socket.listen(1) 
print(f"[*] Listening on {HOST}:{PORT}") 
 
conn, addr = server_socket.accept() 
print(f"[+] Connection established with {addr}") 
 
filename = conn.recv(1024).decode() 
print(f"Receiving file: {filename}") 
 
with open("received_" + filename, "wb") as f: 
    while True: 
        data = conn.recv(1024) 
        if not data: 
            break 
        f.write(data) 
 
print("[+] File received successfully.") 
conn.close() 
server_socket.close() 