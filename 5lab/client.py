import socket as s
from SETTINGS import *
from threading import Thread
import time

client = s.socket(s.AF_INET,s.SOCK_STREAM)
client.connect((IP,PORT))

def FromServer():
	while True:
		in_data = client.recv(MSIZE).decode()
		if in_data=="":
			exit()
		print(f"\u001b[33;1mServer\u001b[37;1m ---> \u001b[33;1m{in_data}\u001b[0m\n")

def ToServer():
	while True:
		time.sleep(.1)
		output_data = input("\u001b[34;1m\n>")
		print(end="\u001b[0m")
		if output_data=="!exit":
			exit()
		client.sendall(bytes(output_data,"UTF-8"))


def draw(IP,PORT):
	format_ip =str(IP)+ " "*(42-len(str(IP)))+"*/"
	format_port =str(PORT)+ " "*(40-len(str(PORT)))+"*/"

	print(f"""\033[32;1m
/**************************************************/
/*                Клиент запущен                  */
/*                                                */
/*                                                */
/*   IP:{format_ip}
/*                                                */   
/*   PORT:{format_port}
/*                                                */
/*                                                */
/**************************************************/\u001b[0m""")

	



draw(IP,PORT)
gets = Thread(target=FromServer,daemon=True)
t2 = Thread(target=ToServer)
gets.start()
t2.start()
