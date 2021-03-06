from platform import system as system_name 
from os import system as system_call
import socket, datetime, gps, sys, time, Adafruit_DHT, requests

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
sensor = Adafruit_DHT.DHT11
hostname = socket.gethostname()

pin = 23
lat = 0
lon = 0
time = 0

def gps():
 x = 1
 while x == 1:
  report = session.next()
  if report['class'] == 'TPV':
   if hasattr(report, 'time'):
    print 'Hora:      ' + str(report.time)
    global time
    time = str(report.time)
   if hasattr(report, 'lat'):
    print 'Latitud:   ' + str(report.lat)
    global lat
    lat = str(report.lat)
   if hasattr(report, 'lon'):
    print 'Longitud:  ' + str(report.lon)
    global lon
    lon = str(report.lon)
   if hasattr(report, 'speed'):
    print 'Velocidad: ' + str(report.speed)
   if hasattr(report, 'track'):
    print 'Rumbo:     ' + str(report.track)
   if hasattr(report, 'head'):
    print report.head
   x= 0

def traceroute(hostname, port, max_hops):
    destination = socket.gethostbyname(hostname)
    print "target %s" % hostname
 
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    ttl = 1
 
    while True:
        recvsock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        sendsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        sendsock.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        recvsock.bind(("", port))
        sendsock.sendto("", (hostname, port))
        currentaddr = None
        currenthostname = None
        try:
            _, currentaddr = recvsock.recvfrom(512)
            currentaddr = currentaddr[0]
 
            try:
                currenthostname = socket.gethostbyaddr(currentaddr)[0]
            except socket.error:
                currenthostname = currentaddr
        except socket.error:
            pass
        finally:
            sendsock.close()
            recvsock.close()
 
        if currentaddr is not None:
            currenthost = "%s (%s)" % (currenthostname, currentaddr)
        else:
            currenthost = "*"
        print "%dt%s" % (ttl, currenthost)
 
        ttl += 1
        if currentaddr == destination or ttl > max_hops:
            break


def ping(host):
    parameters = "-n 1" if system_name().lower()=="windows" else "-c 1"
    return system_call("ping " + parameters + " " + host) == 0

all_data = open('all_data.txt', 'a')
lost_data = open('lost_data.txt', 'a')
send_data = open('send_data.txt', 'a')

try:
	counter = 0
	while counter < 100:
		humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
		ping_server = ping("www.bitsobet.com")
		ping_google = ping("google.com")
		gps()
		all_data.write(str(time) + " " + str(lat) + " " + str(lon) + " " + str(humedad) + " " + str(temperatura) + " " + str(hostname) + " " + str(ping_server) + " " + str(ping_google) + "\n")
		r = requests.post("http://www.bitsobet.com/maps/", data={'temp': temperatura, 'hum': humedad, 'longitud' : lon, 'latitud' : lat, 'humsuelo' : 0, 'precipitacion' : 6, 'datemed' : time})
		if r.status_code == 200:
			send_data.write(str(time) + " " + str(lat) + " " + str(lon) + " " + str(humedad) + " " + str(temperatura) + " " + str(hostname) + " " + str(ping_server) + " " + str(ping_google) + "\n")
		else:
			lost_data.write(str(time) + " " + str(lat) + " " + str(lon) + " " + str(humedad) + " " + str(temperatura) + " " + str(hostname) + " " + str(ping_server) + " " + str(ping_google) + "\n")
		counter += 1
	all_data.close()
	lost_data.close()
	send_data.close()

except Exception,e:
	print str(e)

