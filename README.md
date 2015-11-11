Archivos utilizados para el registro de condiciones climaticas del primer convector solar de la E.E.T Henry Ford.
Presentado en la exposición de los 50 años.

Este software fue utilizado en una Raspberry Pi 2 con el S.O. Minibian Wheezy.
Además, se utilizó un Arduino UNO que enviaba 4 datos de temperatura por serie. Los sensores utilizados fueron DS18B20
en modo parasito y todos conectados al mismo PIN del Arduino (PIN 2)
Los datos fueron enviados a la pagina thingspeak.com para hace un grafico con cada uno de los datos, y luego adaptamos los graficos
a una pagina HTML propia.

Todo el software es de libre uso para cualquier alumno de la E.E.T Henry Ford.

Troubleshooting:

Para poder usar sensores I2C en Raspberry Pi, se deben realizar los siguientes pasos por medio del terminal:

Ejecutar comando: sudo nano /etc/modules
agregar al final del archivo: 
i2c-bcm2708 
i2c-dev
Usar control X -> Y para guardar y cerrar el editor de texto.
Ejecutar comando sudo raspi-config
Navegar en el menu hasta: Advanced Options -> I2C -> Yes -> Yes.
Cerrar la configuracion y ejecutar el comando: sudo reboot

Dependiendo de la distribución de Linux utilizada, puede ser que el sistema solicite la contraseña root para ejecutar comandos
con sudo. En el caso de Minibian, la contraseña por default es raspberry

Para descargar las ultimas librerias de los sensores BMP180 o DHT22 (AM2302), utilizar cualquiera de los siguientes comandos segun que sensor se va a utilizar

git clone https://github.com/adafruit/Adafruit_Python_BMP.git
git clone https://github.com/adafruit/Adafruit_Python_DHT.git

Para instalar el software de los sensores DHT22 (AM2302) o BMP180, navegar hasta el directorio del sensor deseado, y luego
ejecutar los siguientes comandos:

sudo apt-get update
sudo apt-get install git build-essential python-dev python-smbus
sudo python setup.py install

Para probar si el sensor funciona, navegar hasta la carpeta examples/ y ejecutar el comando:

sudo python simpletest.py


