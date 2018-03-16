from platform import system as system_name
from os import system as system_call

def ping(host):
    parameters = "-n 1" if system_name().lower()=="windows" else "-c 1"
    return system_call("ping " + parameters + " " + host) == 0

ping("google.com")
print(ping("google.com"))