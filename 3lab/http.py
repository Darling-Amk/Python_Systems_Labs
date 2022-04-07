#!/usr/bin/python3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("www.google.com", 80))

sock.send(b"HEAD / HTTP/1.1\r\nHost:www.google.com\r\n\r\n")

response = sock.recv(4096)

sock.close()

print(response.decode())