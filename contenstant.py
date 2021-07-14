import socket
import sys
import threading 

contestant = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cname = socket.gethostname()    
caddr = socket.gethostbyname(cname)    

haddr=raw_input("Enter host IP address:\n")
hport=input("Enter the port where the host program is running")

contestant.connect((haddr,hport))

def message():
	while True :
		msg=raw_input()
		contestant.send(name+" : "+msg)
def read():
	var=0
	while True :
		if not  var:
			msg=contestant.recv(2048)
			global name 
			name = msg[3]
			var=1;
			print (msg)
		else:
			msg=contestant.recv(2048)
			print(msg)

sending =threading.Thread(target=message).start()
recieving=threading.Thread(target=read).start()
