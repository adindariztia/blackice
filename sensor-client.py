###################################################
####### Temperature & Humidity client sensor ######
####### Author: Adinda Riztia Putri ###############
###################################################

import time
from time import gmtime, strftime
import board
import adafruit_dht
import socket
import json


# initialize the sensor
dhtdevice = adafruit_dht.DHT11(board.D23)

#remote server IP address and port
HOST = "202.31.134.217"
PORT = 2508

# initialize socket connection to server
s = socket.socket()
s.connect((HOST, PORT))

while True:
    try:
        tempCelcius = dhtdevice.temperature #get current temperature reading
        humidity = dhtdevice.humidity #get current temperature reading
        timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #get current time reading
        
        # store the data in a json object for easier data handling cia cia ciaa
        sensor_data = {
            "timestamp": timestamp,
            "temperature": tempCelcius,
            "humidity": humidity
        }
        
        data = json.dumps(sensor_data)
        
        #print sensor reading value for log info
        print( timestamp +
            " Temp: {:.1f} C    Humidity: {}% ".format(
                tempCelcius, humidity
            )
        )
        s.send(bytes(data,encoding="utf-8")) #send the data to remote server
        data = s.recv(1024)
            
        print("dapet data neh ", data)
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1)
        continue
    except Exception as error:
        print(error.args[0])
        dhtdevice.exit()
        raise error
    
    time.sleep(1)