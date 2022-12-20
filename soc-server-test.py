import socket
import json

HOST = "202.31.134.217" 
PORT = 2508

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            tmpStr = data.decode()
            jsonObj = json.loads(tmpStr)
            
            if not data:
                break
            conn.send(data)