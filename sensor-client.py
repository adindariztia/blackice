import time
from time import gmtime, strftime
import board
import adafruit_dht
import socket


# initialize the sensor
dhtdevice = adafruit_dht.DHT11(board.D23)

#remote server IP address and port
HOST = "202.31.134.217"
PORT = 2508

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))

# s = socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
s = socket.socket()
s.connect((HOST, PORT))

while True:
    try:
        tempCelcius = dhtdevice.temperature
        humidity = dhtdevice.humidity
        timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        sensor_data = {
            "timestamp": timestamp,
            "temperature": tempCelcius,
            "humidity": humidity
        }
        
        print( timestamp +
            " Temp: {:.1f} C    Humidity: {}% ".format(
                tempCelcius, humidity
            )
        )
        s.send(sensor_data)
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