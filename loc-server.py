import socket
import time
import json

HOST = "127.0.0.1" 
PORT = 2508

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            test = data.decode()
            jsonObj = json.loads(test)
            print(jsonObj["data"])
            # print(type(data))
            if not data:
                break
            conn.send(data)