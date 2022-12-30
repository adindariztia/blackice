###################################################
####### Temperature & Humidity client sensor ######
####### Author: Adinda Riztia Putri ###############
###################################################


import time
from datetime import datetime
from time import gmtime, strftime
import board
import adafruit_dht
import socket
import json
import csv

# initialize the sensor
dhtdevice = adafruit_dht.DHT11(board.D23)

def saveData(data):
    now = datetime.now()
    with open('dht11_dataset_{}.csv'.format(now.strftime("%Y-%m-%d")), 'a', encoding='UTF8') as f:
        writer =csv.writer(f, delimiter=';')
        writer.writerow([data["timestamp"], data["temperature"], data["humidity"]])

while True:
    try:
        tempCelcius = dhtdevice.temperature #get current temperature reading
        humidity = dhtdevice.humidity #get current temperature reading
        timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #get current time reading
    
        sensor_data = {
            "timestamp": timestamp,
            "temperature": tempCelcius,
            "humidity": humidity
        }
        
        #print sensor reading value for log info
        print( timestamp +
            " Temp: {:.1f} C    Humidity: {}% ".format(
                tempCelcius, humidity
            )
        )
        
        saveData(sensor_data)
            

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1)
        continue
    except Exception as error:
        print(error.args[0])
        dhtdevice.exit()
        raise error
    
    time.sleep(1)