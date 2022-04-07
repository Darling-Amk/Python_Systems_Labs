#!/usr/bin/python3
import DNS
import socket
import sys

if len(sys.argv)!=2:
	print('Должен быть 1 аргумент')
	exit(1)

host = sys.argv[1]

req = DNS.DnsRequest(name=host)
r = req.req()
r.show()
print(r.answers)