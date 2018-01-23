import socket
import datetime

all_data = open('all_data.txt', 'a')
lost_data = open('lost_data.txt', 'a')
send_data = open('send_data.txt', 'a')

now = datetime.datetime.now()
print(now.hour, now.minute, now.second)

#TODO
"""
hora latitud longitud humedad hostname resultadoping fullping traceroute 
3 archivos: todos los datos, enviados a servicio, perdidos
"""

hostname = socket.gethostname()
#file.write(socket.gethostname() + '\n')
all_data.close()
lost_data.close()
send_data.close()

from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that some hosts may not respond to a ping request even if the host name is valid.
    """

    # Ping parameters as function of OS
    parameters = "-n 1" if system_name().lower()=="windows" else "-c 1"

    # Pinging
    return system_call("ping " + parameters + " " + host) == 0

#print(ping("google.com"))