#!/usr/bin/python3
import socketserver
import socket
import json
import time
import sys
from threading import Thread
from ...environment.world import *
from ...environment.natural_laws.constants import Constants
from ...utilities.utilities import *

class ClientThreadRequest(socketserver.BaseRequestHandler):
    """
    It allows  handle several clients at the same time using a new thread for each new connection
    """
    def handle(self):
        #from environment.common_space import Request
        print('New thread started for request of: ', self.client_address[0])
        try:
            c = Constants()
            data = json.loads(receive_end(self.request), strict=False)
            message = Request.solve(data) + c.end_marker
            self.request.sendall(message.encode('utf8'))
            print('Request : %s finished!' % data[0])
        except socket.error as e:
            print("Error sending data: %s" % e)
        finally:
            print('Waiting for new requests...')

#####################################################################


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    socketserver.TCPServer.address_family = socket.AF_INET6
    pass

#####################################################################


def receive_end(the_socket):
    """
    Receive complete information ia socket using marker END.
    """
    c = Constants()
    end = c.end_marker
    total_data = []
    data = ''
    while True:
            data = the_socket.recv(c.block_size).decode('utf8')
            if end in data:
                total_data.append(data[:data.find(end)])
                break
            total_data.append(data)
            if len(total_data) > 1:
                #check if end_of_data was split
                last_pair = total_data[-2] + total_data [-1]
                if end in last_pair:
                    total_data[-2] = last_pair[:last_pair.find(end)]
                    total_data.pop()
                    break
    return ''.join(total_data)

#####################################################################


def receive_time_out(server_socket, timeout=4):
    """
    Receive all data sent through a socket using time out as parameter
    """
    server_socket.setblocking(0)
    total_data = []
    begin = time.time()
    c = Constants()
    while True:
        #if you got some data, then break after wait sec
        if total_data and time.time() - begin > timeout:
            break
        #if you got no data at all, wait a little longer
        elif time.time() - begin > timeout *4 :
            break
        try:
            data = server_socket.recv(c.block_size)
            if data:
                total_data.append(data.decode('utf8'))
                begin = time.time()
            else:
                time.sleep(0.1)
        except:
            pass
    return ''.join(total_data)


#####################################################################


def create_message(address, request, data=''):
    """
    Check  if the tlon0 interface is available
    """
    c = Constants()
    if is_inet('tlon0'):
        # ad hoc network message
        host = (address, c.port, 0, 5)
    elif is_inet('bridge100'):
        host = (address, c.port, 0, 10)
    else:
        # local message
        host = (address, c.port, 0, 1)

    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
    message = list()
    message.append(request)
    message.append(data)
    m = json.dumps(message) + c.end_marker

    try:
        s.settimeout(c.time_out)  # set maximum timeout
        s.connect(host)
    except Exception as e:
        print("[ERROR]: %s" % e)
        sys.exit(0)

    try:
        s.sendall(m.encode('utf8'))
        data = json.loads(receive_end(s), strict=False)
    except Exception as e:
        print("Error sending data: %s" % e)

    finally:
        s.close

    return data
