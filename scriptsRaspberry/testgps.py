import gps

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
x= 1

while x == 1:
 report = session.next()
 if report['class'] == 'TPV':
  if hasattr(report, 'time'):
   print 'Hora:      ' + str(report.time)
  if hasattr(report, 'lat'):
   print 'Latitud:   ' + str(report.lat)
  if hasattr(report, 'lon'):
   print 'Longitud:  ' + str(report.lon)
  if hasattr(report, 'speed'):
   print 'Velocidad: ' + str(report.speed)
  if hasattr(report, 'track'):
   print 'Rumbo:     ' + str(report.track)
  if hasattr(report, 'head'):
   print report.head
  x= 0
