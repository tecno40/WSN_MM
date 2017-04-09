# Send UDP broadcast packets
 

MYPORT = 50000
 
import sys, time
from socket import *
 
myip = "127.0.0.1"
print(myip)
 
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('', MYPORT))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
 
while 1:
    data = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" + '\n'
    data2 ="111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111" + '\n'
#    s.sendto(data, ('<broadcast>', MYPORT))
    s.sendto(data.encode(), ('<broadcast>', MYPORT))
    s.sendto(data2.encode(), ('<broadcast>', MYPORT))

    print ('server sent %r to %r' % (data, '<broadcast>'))
    #time.sleep(2)
 
    data, addr = s.recvfrom(1024)
    ip, port = addr
    print (myip, ip)
    if ip == myip:
        print ('server received %r from myself' % (data))
    else:
        print ('server received %r from %r' % (data, ip))