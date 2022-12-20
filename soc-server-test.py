############################################################
####### Temperature & Humidity data collection server ######
####### Author: Adinda Riztia Putri ########################
############################################################

import socket
import json
import csv

#remote server IP address and port
HOST = "202.31.134.217" 
PORT = 2508

#to store the transmitted sensor data into csv
def saveData(data):
    with open('dataset_sensor.csv', 'a', encoding='UTF8') as f:
        writer =csv.writer(f, delimiter=';')
        writer.writerow([data["timestamp"], data["temperature"], data["humidity"]])

#open connection to listen for incoming connection        
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    
    conn, addr = s.accept() #accept incoming connection
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            tmpStr = data.decode() #decode from data format byte
            jsonObj = json.loads(tmpStr) #save to json object
            saveData(jsonObj) #save data to csv
            if not data:
                break
            conn.send(data)
            
