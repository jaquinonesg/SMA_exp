from platform import system as system_name 
from os import system as system_call
import socket, datetime, gps, sys, time, Adafruit_DHT, requests

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
x= 1

while x == 1:
 report = session.next()
 if report['class'] == 'TPV':
  if hasattr(report, 'time'):
   print 'Hora:      ' + str(report.tim1e)
  if hasattr(report, 'lat'):
   print 'Latitud:   ' + str(report.lat)
   lat = str(report.lat)
  if hasattr(report, 'lon'):
   print 'Longitud:  ' + str(report.lon)
   lon = str(report.lon)
  if hasattr(report, 'speed'):
   print 'Velocidad: ' + str(report.speed)
  if hasattr(report, 'track'):
   print 'Rumbo:     ' + str(report.track)
  if hasattr(report, 'head'):
   print report.head
  x= 0

# Configuracion del tipo de sensor DHT
sensor = Adafruit_DHT.DHT11

# Configuracion del puerto GPIO al cual esta conectado  (GPIO 23)
pin = 23

# Intenta ejecutar las siguientes instrucciones, si falla va a la instruccion except
try:
	# Ciclo principal infinito
	while True:
		# Obtiene la humedad y la temperatura desde el sensor
		humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
		# Imprime en la consola las variables temperatura y humedad con un decimal
		
		r = requests.post("http://www.bitsobet.com/maps/", data={'temp': temperatura, 'hum': humedad, 'longitud' : lon, 'latitud' : lat, 'humsuelo' : 0, 'precipitacion' : 6, 'datemed' : '2018-02-02T12:55:29.000Z'})
		#print("El servicio web no puede ser alcanzado")
		# Duerme 10 segundos
		time.sleep(5)

# Se ejecuta en caso de que falle alguna instruccion dentro del try
except Exception,e:
	# Imprime en pantalla el error e
	print str(e)