import time
from time import gmtime, strftime
import board
import adafruit_dht


# initialize the sensor
dhtdevice = adafruit_dht.DHT11(board.D23)

while True:
    try:
        tempCelcius = dhtdevice.temperature
        humidity = dhtdevice.humidity
        timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print( timestamp +
            " Temp: {:.1f} C    Humidity: {}% ".format(
                tempCelcius, humidity
            )
        )
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1)
        continue
    except Exception as error:
        print(error.args[0])
        dhtdevice.exit()
        raise error
    
    time.sleep(1)