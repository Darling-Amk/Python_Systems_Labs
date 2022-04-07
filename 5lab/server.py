import socket as s
import threading
from SETTINGS import *


# Описание работы сервера
server = s.socket(s.AF_INET,s.SOCK_STREAM)
server.bind((IP,PORT))
class ClientThreader(threading.Thread):
	def __init__(self,addres,user_sock):
		self.username = f"{addres[0]}:{addres[1]}"
		print(f"\n\u001b[35;1mНовое подключение:\n----->{self.username}\u001b[0m")
		threading.Thread.__init__(self)
		self.csocket = user_sock

	def run(self):
		try:
			while True:
				data = self.csocket.recv(MSIZE)
				msg = data.decode()
			
				if msg=="":
					self.csocket.send(bytes("disconnect","UTF-8"))
					print(f"\n\u001b[31;1mОтключение:\n -----> {self.username}\u001b[0m")
					exit()
				elif "echo" == msg[:4]:
					tmp_msg = msg.replace("echo","")
					print(f"\n\u001b[35;1mECHO\n\u001b[34;1m{self.username}\u001b[37;1m --> \u001b[36;1m{tmp_msg} \u001b[37;1m-->\u001b[37;1m \u001b[34;1m{self.username} \u001b[0m")
					self.csocket.send(bytes(tmp_msg,"UTF-8"))
					continue
				elif "setname" in msg:
					tmp_name = msg.replace('setname',"").replace(" ","")
					print(f"\n\u001b[33;1mСмена псевдонима\n{self.username} ----> {tmp_name}\u001b[0m")
					self.username = tmp_name
					continue
				print(f"\n\u001b[34;1m{self.username}\u001b[37;1m:\u001b[36;1m{msg}\u001b[0m")
		except:
			print(f"\n\u001b[31;1mОтключение:\n<-----{self.username}\u001b[0m")
			

format_ip =str(IP)+ " "*(42-len(str(IP)))+"*/"
format_port =str(PORT)+ " "*(40-len(str(PORT)))+"*/"
print(f"""\033[32;1m
/**************************************************/
/*                Сервер запущен                  */
/*                                                */
/*                                                */
/*   IP:{format_ip}
/*                                                */   
/*   PORT:{format_port}
/*                                                */
/*                                                */
/**************************************************/\u001b[0m""")


while True:
	server.listen(1)
	user_sock,addres = server.accept()
	newthreed = ClientThreader(addres,user_sock)
	newthreed.start()