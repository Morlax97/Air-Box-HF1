import Adafruit_BMP.BMP085 as BMP085
import smbus
import time
import httplib
import urllib

sensor = BMP085.BMP085()

DEVICE     = 0x23 # Default device I2C address
POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value

# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_1 = 0x20

bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number
  return ((data[1] + (256 * data[0])) / 1.2)

def readLight(addr=DEVICE):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
  return convertToNumber(data)

def main():
	 Temp = sensor.read_temperature()
         Pressure = sensor.read_pressure()
         LightLevel = readLight()
	 params = urllib.urlencode({'field1': Temp,'field2': Pressure,'field3': LightLevel, 'key':'SO8KZPRKB3KDSBOZ'})
	 headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
	 conn = httplib.HTTPConnection("api.thingspeak.com:80")     
	 try:
		 conn.request("POST", "/update", params, headers)
		 response = conn.getresponse()
		 print Temp
		 print Pressure
		 print LightLevel 
		 print response.status, response.reason
		 data = response.read()
		 conn.close()
	 except:
		 print "connection failed"

if __name__ == "__main__":
	while True:
		main()
		time.sleep(30)
