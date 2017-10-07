#!/usr/bin/python3
import socket
from ...environment.world import *
import netifaces
from ...utilities.utilities import *
from threading import Thread
import platform
import subprocess
import psutil as ps


def get_ipv4_interface():
    """
    Check ipv4 address of the selected interface
    """
    if is_inet('tlon0'):
        return netifaces.ifaddresses('tlon0')[netifaces.AF_INET][0]['addr']
    elif is_inet('bridge100'):
        return netifaces.ifaddresses('bridge100')[netifaces.AF_INET][0]['addr']
    else:
        return netifaces.ifaddresses('lo')[netifaces.AF_INET][0]['addr']

#####################################################################


def get_ipv6_interface():
    """
    Checks the ipv6 address of the selected interface
    """
    if is_inet('tlon0'):
        return netifaces.ifaddresses('tlon0')[netifaces.AF_INET6][0]['addr'].replace('%tlon0','')
    elif is_inet('bridge100'):
        return netifaces.ifaddresses('bridge100')[netifaces.AF_INET6][0]['addr'].replace('%bridge100','')
    else:
        return netifaces.ifaddresses('lo')[netifaces.AF_INET6][0]['addr']
#####################################################################

def mac_to_ipv6(mac):
    """
    Convert mac address to ipv6 address
    """
    # only accept MACs separated by a colon
    parts = mac.split(":")
    # modify parts to match IPv6 value
    parts.insert(3, "ff")
    parts.insert(4, "fe")
    parts[0] = "%x" % (int(parts[0], 16) ^ 2)

    # format output
    ipv6Parts = []
    for i in range(0, len(parts), 2):
        ipv6Parts.append("".join(parts[i:i + 2]))
    ipv6 = "fe80::%s" % (":".join(ipv6Parts))
    return ipv6


#####################################################################


def get_info_local_machine():
    """
    This method return basic information of local machine
    """
    ipv4local_address = get_ipv4_interface()
    ipv6local_address = get_ipv6_interface()
    name = socket.gethostname()
    system = platform.system()
    release = platform.release()
    return ipv4local_address, ipv6local_address, name, system, release


#####################################################################


def get_resources_local_machine():
    """
       Function developed by German Dario Alvarez

       This function gives you information about most of the machine resources
       The function tree is based on levels, so you can call the function and drill down
       according to your needs, check the example below:

       ¿I want to know total memory of device and assign to x variable?

       level_1: mem
       level_2: mem
       level_3: index0

       x= get_machine_resources()
       x["mem"]["mem"][0]

           use:
       info = get_machine_resources()

       info["cpu"]["percent"]      # percentage usage by cpu
       info["cpu"]["cores"]	       # number of cores
       info["cpu"]["freq"]	        # CPU frequency

       info["mem"]["mem"]	        # ram distribution
       info["mem"]["swap"]	        # reserverd swap memory

       info["net"]["io"]	        # I/O on sockets and network
       info["net"]["conn"]	        # Active connections on sockets
       info["net"]["addr"]	        # Interfaces address
       info["net"]["stats"]	    # Networking stats

       info["battery"]["bat"]	    # battery information if device has one
       info["battery"]["temp"]	    # temm88
       perature status for device

       info["disk"]["parts"]	    # Partitions of the hard disk
       info["disk"]["usage"]	    # Usage on / root partition
       info["users"]		        # Users information
       """

    sys_info = {}
    # CPU INFORMATION
    cpu_percent = ps.cpu_percent(percpu=True)
    cpu_cores = ps.cpu_count()
    cpu_freq = ps.cpu_freq()
    sys_info["cpu"] = {"percent": cpu_percent, "cores": cpu_cores, "freq": cpu_freq}

    # RAM MEMORY INFORMATION
    mem_info = ps.virtual_memory()
    swap_info = ps.swap_memory()
    sys_info["mem"] = {"mem": mem_info, "swap": swap_info}

    # NETWORK INFORMATION
    ip_io_info = ps.net_io_counters()
    ip_conn_info = ps.net_connections(kind='inet')
    ip_info = ps.net_if_addrs()
    ip_stats_info = ps.net_if_stats()
    sys_info["net"] = {"io": ip_io_info, "conn": ip_conn_info, "addr": ip_info, "stats": ip_stats_info}

    # BATTERY AND SENSORS INFORMATION
    battery_info = ps.sensors_battery()
    temperature_info = ps.sensors_temperatures()
    sys_info["battery"] = {"bat": battery_info, "temp": temperature_info}

    # DISKS INFORMATION
    disk_partitions = ps.disk_partitions()
    disk_usage = ps.disk_usage('/')
    disk_io = ps.disk_io_counters()
    sys_info["disk"] = {"parts": disk_partitions, "usage": disk_usage, "io": disk_io}

    # USERS INFORMATION
    sys_info["users"] = ps.users()

    return sys_info

#####################################################################


@is_batman_running
def get_active_nodes():
    """
    Search active nodes the ad hoc network
    """
    active_nodes = list()

    try:
        active_nodes = subprocess.getoutput('sudo bash ../network/get_batman_nodes.bash')
    except subprocess.SubprocessError as e:
        print('Problem getting batman nodes', e)

    nodes = active_nodes.split('\n')[0].split()
    time_node = active_nodes.split('\n')[1].split()

    if len(nodes) != len(time_node):
        for i in range(len(time_node), len(nodes)):
            time_node.append('-1')

    batman_nodes = list()

    for i in range(len(nodes)):
        temp = list()
        temp.append(mac_to_ipv6(nodes[i]))
        temp.append(time_node[i])
        batman_nodes.append(temp)

    return batman_nodes

#####################################################################


@is_batman_running
def get_info_active_nodes():
    """
    Get basic information of the nodes in the ad hoc network.
    """
    from environment.world import Request
    from environment.communication.socket_methods import create_message
    active_nodes = get_active_nodes()
    info_active_nodes = {}

    for node in active_nodes:
        print(node[0])
        try:
            data = create_message(node[0], Request.NODE_INFO)
            info_active_nodes[node[0]] = data
        except Exception as e:
            info_active_nodes = "There was a problem with the request : "+str(e)
        finally:
            return info_active_nodes

#####################################################################


@is_batman_running
def set_alfred_data(data, datatype):
    """
    Set information in the alfred daemon to flood the network with useful data. To use this script it
    is necessary modify visudo file and allow the user use sudo without password
    """
    if int(datatype) < 64:
        return "Datatype from 0 to 63 are reserved for A.L.F.R.E.D daemon! "
    else:
        try:
            subprocess.getoutput('bash ../network/set_alfred_info.bash ' + data + ' ' + str(datatype))
            return 'data: -' + str(data) + '- is now in datatype: ' + str(datatype)
        except subprocess.SubprocessError as e:
            return 'There is a problem with A.L.F.R.E.D daemon:' + str(e)

#####################################################################


@is_batman_running
def get_alfred_data(datatype):
    """
    Get information from A.L.F.R.E.D daemon. To use this script it is necessary modify visudo file and
    allow the user use sudo without password
    """
    try:
        info = subprocess.getoutput('bash ../network/get_alfred_info.bash ' + str(datatype))
        info = info.strip('').split('\n')
        return info
    except subprocess.SubprocessError as e:
        return 'There is a problem with A.L.F.R.E.D daemon:' + str(e)

########################################################################


@is_batman_running
def vis_net_topology():
    """
    Get network topology using batman-vis
    """
    try:
        info = subprocess.getoutput(' sudo batadv-vis')
        info = info.split('\n')
        graph = list()
        for i in info:
            if i.find("TT") == -1:
                graph.append(i)
        graph = "\n".join(graph)

        file = open('../network/topology.dot', 'w')
        file.writelines(graph)
        file.close()
        subprocess.getoutput(' dot ../network/topology.dot -o ../network/topology.png -Tpng ')
        return graph
    except IOError as e:
        print(e)
        return "Problems with graphviz " + str(e)

    ######################################################################

@is_batman_running
def set_GPSD():
    # TODO complete this function :(
    pass

######################################################################

@is_batman_running
def get_GPSD():
    # TODO complete this function :(
    pass
