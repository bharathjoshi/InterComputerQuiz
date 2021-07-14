import socket 
import sys 
import thread
import sys
import time 
import timeout_decorator

host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

hostname=socket.gethostname()
ipaddress=socket.gethostbyname(hostname)

try :
	portno=input("Enter port number\n :")
	host.bind((ipaddress,portno))

except OverflowError:
	print("Port no out of range , Try in [0,65535]\n")
	sys.exit()

except:
	print("port not available\n")
	sys.exit()

host.listen(3)
contestants=[]


score=[0,0,0]

def remove_(conn,addr):
	if [conn,addr] in contestants:
		contestants.remove([conn,addr])

def broadcast(message,conn,addr,index):
	for members in contestants:
		if index==0 :
			if members[1]!=conn:
				try :
					members[1].send(message)
				except :
					members[1].close()
					remove_(members[1],members[2])
		else :
			try :
				members[1].send(message)
			except :
				members[1].close()
				remove_(members[1],members[2])
	
def main ():

lst ,[] ,[] = select.select([contestants],[],[],60) 

 if(len(lst) > 0)
 

while(True):
	conn,addr=host.accept()
	contestants.append(conn)
	
def contest:
	for i i:
		broadcast
		lst ,[] ,[] = select.select([contestants],[],[],60) 
		if(len(lst) > 0)


