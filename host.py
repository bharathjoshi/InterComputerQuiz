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

def questions():
	if (len(contestants)==3) :
		que=[1,2,3,4,5,6,7,8,9,10]
		for i in range(10):
			broadcast(que[i],1,1,1)


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



def work (conn,addr):
	
	conn.send("Hi " +chr(len(contestants)+64)+" You are entering into the contest. The person who ll be first answering may only get the point(if one is correct)")

	while True :
		try : 
			answers=[]
			message=conn.recv(2048)
			if message :
				print(message)
				broadcast(message,conn,addr,0)
			else:
				remove_(conn)
		except :
			continue



while(True):
	conn,addr=host.accept()
	contestants.append([chr(65+len(contestants)),conn,addr])
	print(conn)
	print(type(conn))

	print(addr[0]+" connected")
	thread.start_new_thread(work,(conn,addr))
	thread.start_new_thread(questions,())
	

conn.close()
host.close()

