from platform import system as system_name 
from os import system as system_call
import socket
import datetime


all_data = open('all_data.txt', 'a')
lost_data = open('lost_data.txt', 'a')
send_data = open('send_data.txt', 'a')


#TODO
"""
hora latitud longitud humedad temperatura hostname resultadoping fullping traceroute
3 archivos: todos los datos, enviados a servicio, perdidos
"""

#hostname
#file.write(socket.gethostname() + '\n')


#print(ping("google.com"))

all_data.close()
lost_data.close()
send_data.close()
