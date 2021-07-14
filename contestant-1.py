import socket
import sys
import threading 
import select

contestant = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

haddr=raw_input("Enter host IP address:\n")
hport=input("Enter the port where the host program is running:\n")

contestant.connect((haddr,hport))
index=0;
count=0;
while True : 
	socket_list=[sys.stdin,contestant]
	read_s,write_s ,error_s = select.select(socket_list,[],[])

	for socks in read_s :
		if socks== contestant :
			message = socks.recv(2048)
			if not index :
				name=message;
				index=1;
			print message
		else :
			message=sys.stdin.readline()
			if message :
				inside_conn= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				inside_conn.connect((haddr,hport))
				inside_conn.send(name+" : "+message)
				inside_conn.close()
			sys.stdout.write("<You>") 
			sys.stdout.write(message) 
			sys.stdout.flush() 
