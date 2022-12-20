import socket
HOST = "127.0.0.1"
PORT = 2508
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) 
    while True:
        
        s.send(b"hai adinda")
        data = s.recv(1024)
            
        print("dapet data neh ", data)