# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:47:07 2018
Send File
@author: luc2
"""

import socket

file = open("p2p.py", "rb")
sock = socket.socket()
sock.connect(("127.0.0.1", 8021))

while True:
    chunk = file.read(65536)
    if not chunk:
        break  # EOF
    sock.sendall(chunk)