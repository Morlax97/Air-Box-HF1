# test
# Codigo para enviar los datos de 4 sensores de temperatura DS180B20 conectados en serie con un Arduino UNO,
# y un sensor de luz BH1750 a thingpseak. Modificar la API key por la del canal propio para probar el programa.

import smbus
import time
import httplib
import urllib
import serial

ser = serial.Serial('/dev/ttyACM0', 9600) # definir la ubicación serie del Arduino y la frecuencia. Modificar segun necesidad.

DEVICE     = 0x23   # definir direcciones del BH1750. obtenidas del datasheet.
POWER_DOWN = 0x00
POWER_ON   = 0x01
RESET      = 0x07
ONE_TIME_HIGH_RES_MODE_1 = 0x20

bus = smbus.SMBus(1)

def convertToNumber(data): 
 return ((data[1] + (256 * data[0])) / 1.2) # formula para convertir lo medido por el BH1750 a su valor en lux.

def readLight(addr=DEVICE):  # codigo que mide el sensor BH1750
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
  return convertToNumber(data)

def main():
         time.sleep(2) # sleep necesario para evitar problemas de sincronizacion entre Raspberry y Arduino
         ser.write('1') # El programa del arduino espera la entrada '1' antes de medir los sensores y enviarlos
         text = ser.readline()
         temp1, temp2, temp3, temp4 = text.split(',') # Separación de los datos de los sensores en 4 variables.
	 print text
         LightLevel = readLight() 
         params = urllib.urlencode({'field1': temp1,'field2': temp2,'field3': temp3,'field4': temp4,'key':'SO8KZPRKB3KDSBOZ'}) # estructura de datos para thingspeak. Modificar key por la del canal.
         headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
         conn = httplib.HTTPConnection("api.thingspeak.com:80")
         try:
                 conn.request("POST", "/update", params, headers)
                 response = conn.getresponse()
                 print temp1
                 print temp2
                 print temp3
                 print temp4
                 print LightLevel
                 print response.status, response.reason
                 data = response.read()
                 conn.close()
         except:
                 print "connection failed"

if __name__ == "__main__":
        main()


