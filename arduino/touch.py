import serial
import time
ser = serial.Serial('/dev/ttyACM0', 230400)
time.sleep(2)
ser.write('1')

text = ser.readline()
print text
temp1, temp2, temp3, temp4 = text.split(',')
print temp1
print temp2
print temp3
print temp4

