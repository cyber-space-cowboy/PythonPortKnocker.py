#!/usr/bin/python
import socket
ip = []
port = []
x=0
number = int(input("How many IPs are you testing: "))
for i in range (0, number):
        uip = socket.inet_aton(raw_input("Enter the ip: "))
        ip.append(uip)
        print "IP", ip

num = int(input("How many ports are you testing: "))
for i in range (0, num):
        uport = int(raw_input("Enter the port: "))
        port.append(uport)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for x in range(len(ip)):
        irange = socket.inet_ntoa(ip[x])
        nrange = socket.gethostbyname(irange)
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for y in range(len(port)):
                iport = port[y]
                rhost = s.connect_ex((nrange, iport))
                if rhost == 0:
                        print "IP: ", irange," Port: ", iport, " is open"
                        with open('output_python.txt', 'a') as f:
                                print >>f, "IP: ", irange," Port: ", iport, " is open"
                        f.close()
                        y += 1

                else:
                        print "IP: ", irange," Port: ", iport, " is closed"
                        with open('output_python.txt', 'a') as f:
                                print >>f, "IP: ", irange," Port: ", iport, "is closed" 
                        f.close()
                        y += 1
                #s.close()


        x += 1

