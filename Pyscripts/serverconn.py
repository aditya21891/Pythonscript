#!/usr/bin/env python3

import socket
HOST = '127.0.0.1'  # The server's hostname or IP address
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 8080))
serv.listen(5)
