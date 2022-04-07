import socket as s
import sys
from threading import Thread
import time

def main(argv):
	HOST = "www.google.com" if len(argv) == 0 else argv[0]

	PORT = 80
	MSIZE = 1024
	client = s.socket(s.AF_INET,s.SOCK_STREAM)
	#Для преобразования доменного имени (и, если необходимо, имени сервиса) в IP-адрес и номер порта в предыдущем задании используйте функцию getaddrinfo()
	target = s.getaddrinfo(HOST, PORT)
	if(HOST=="localhost"):
		target = [[[1],[2],[3],[4],("localhost",80)]]

	client.connect(target[0][4])

	def HTTP():
		draw(*target[0][4],MSIZE)
		print("\u001b[36;1mGET\u001b[37;1m/\u001b[36;1mHEAD\u001b[37;1m/\u001b[36;1mEXIT\u001b[0m")
		while True:
			command = input("\u001b[35;1m>")
			if command=="EXIT":
				print(end="\u001b[0m")
				exit()
			elif command=='GET':
				client.sendall(bytes(f"GET / HTTP/1.1\r\nHost:{HOST}\r\n\r\n","UTF-8"))
				time.sleep(1)
			elif command=='HEAD':
				client.sendall(bytes(f"HEAD / HTTP/1.1\r\nHost:{HOST}\r\n\r\n", "UTF-8"))
				time.sleep(1)
			print(end="\u001b[0m")

	def FromServer():
		while True:
			try:
				in_data = client.recv(MSIZE).decode()
			except:
				in_data = ""
				continue
			print(f"\u001b[33;1mServer\u001b[37;1m ---> \u001b[33;1m{in_data}\u001b[0m\n")

	listen = Thread(target=FromServer,daemon=True)
	request = Thread(target=HTTP)
	listen.start()
	request.start() 

def draw(IP,PORT,SIZE):
	IP =str(IP)+ " "*(42-len(str(IP)))+"*/"
	PORT =str(PORT)+ " "*(40-len(str(PORT)))+"*/"
	SIZE = str(SIZE)+" "*(34-len(str(SIZE)))+"*/"
	print(
		f"""\033[32;1m
/**************************************************/
/*                Клиент запущен                  */
/*                                                */
/*                                                */
/*   IP:{IP}
/*                                                */   
/*   PORT:{PORT}
/*                                                */
/*   CHUNK SIZE:{SIZE}
/*                                                */
/**************************************************/\u001b[0m""")

if __name__=="__main__":
	main(sys.argv[1:])
	
	
