import smbus
import time
import httplib
import urllib
import serial
import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()
ser = serial.Serial('/dev/ttyACM0', 9600)

DEVICE     = 0x23
POWER_DOWN = 0x00
POWER_ON   = 0x01
RESET      = 0x07
ONE_TIME_HIGH_RES_MODE_1 = 0x20
ONE_TIME_LOW_RES_MODE = 0x23

bus = smbus.SMBus(1)

def convertToNumber(data):
  return ((data[1] + (256 * data[0])) / 1.2)

def readLight(addr=DEVICE):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
 # data = bus.read_i2c_block_data(addr,ONE_TIME_LOW_RES_MODE)
  return convertToNumber(data)

def main():
         time.sleep(2)
         ser.write('1')
         text = ser.readline()
         temp1, temp2, temp3, temp4 = text.split(',')
         print text
         LightLevel = readLight()
	 TempAmbiente = sensor.read_temperature()
	 print TempAmbiente
         params = urllib.urlencode({'field1': temp1,'field2': temp2,'field3': temp3,'field4': temp4,'field5': LightLevel,'field6':TempAmbiente,'key':'SO8KZPRKB3KDSBOZ'})
         headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
         conn = httplib.HTTPConnection("api.thingspeak.com:80")
 try:
                 conn.request("POST", "/update", params, headers)
                 response = conn.getresponse()
                # print temp1
                # print temp2
                # print temp3
                # print temp4
                 print LightLevel
                 print response.status, response.reason
                 data = response.read()
                 conn.close()
         except:
                 print "connection failed"

if __name__ == "__main__":
        main()

