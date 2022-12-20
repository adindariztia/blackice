import socket
import json
import csv

HOST = "202.31.134.217" 
PORT = 2508

def saveData(data):
    with open('dataset_sensor.csv', 'a', encoding='UTF8') as f:
        writer =csv.writer(f, delimiter=';')
        writer.writerow([data["timestamp"], data["temperature"], data["humidity"]])
        
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
            saveData(jsonObj)
            if not data:
                break
            conn.send(data)
            
