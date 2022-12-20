import socket
import time
import json

HOST = "127.0.0.1"
PORT = 2508
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) 
    while True:
        adinda = {"data": "adinda riztia lalalalla"}
        data = json.dumps(adinda)
        s.send(bytes(data,encoding="utf-8"))
        data = s.recv(1024)
            
        print("dapet data neh ", data)
        
        time.sleep(1)