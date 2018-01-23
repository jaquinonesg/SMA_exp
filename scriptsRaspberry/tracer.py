#!/usr/bin/python
import sys
import socket
 
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
 
if __name__ == "__main__":
    traceroute(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]