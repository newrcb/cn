import socket
import os

HOST = '127.0.0.1'  
PORT = 5001   

filename = input("Enter filename to send: ")

if not os.path.exists(filename):
    print("File not found!")
    exit()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print(f"[+] Connected to {HOST}:{PORT}")

client_socket.send(filename.encode())

with open(filename, "rb") as f:
    data = f.read(1024)
    while data:
        client_socket.send(data)
        data = f.read(1024)

print("[+] File sent successfully.")
client_socket.close() 
