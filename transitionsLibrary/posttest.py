import requests, time
humedad = 1
temperatura = 1
lon = 1
lat = 1
datetime = '2018-02-02T12:55:29.000Z'

r = requests.post("http://www.bitsobet.com/maps/", data={'temp': temperatura, 'hum': humedad, 'longitud' : lon, 'latitud' : lat, 'humsuelo' : 0, 'precipitacion' : 6, 'datemed' : datetime})
print(r.status_code, r.reason)