# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 17:30:19 2018
Peer to Peer Rewrite: Less convoluted v1.2
@author: luc2
"""
#import socket
import socket, sys

p = socket.socket() #socket object create
host = socket.gethostname() #Ask: localmachine name
port = 12345 #Reserve port name
p.bind((host, port))

if sys.argv[1] == "connect":
    host = sys.argv[2]
    p.connect((host, port))
    p.close 
else:
    p.listen(5)                 # Now wait for client connection.
    while True:
       c, addr = p.accept()     # Establish connection with client.
       print('Got connection from', addr) 
       c.send('Thank you for connecting')
       c.close()

