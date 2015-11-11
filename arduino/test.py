import serial
import time
ser = serial.Serial('/dev/ttyACM0', 230400)
time.sleep(2)
ser.write('1')

text = ser.readline()
print text



# s1, s2, s3, s4 = text.split(",")
# POST s1 s2 s3 s4

