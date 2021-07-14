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

que=[10,20,30,40,50,60,70,80,90,100]
score=[0,0,0]
@timeout_decorator.timeout(5, timeout_exception=StopIteration)
def mytest():
	try:
    		print("Start")
    		for i in range(1,10):
        		time.sleep(1)
        		#print("{} seconds have passed".format(i))
    	except :
	    	return 1;

def recv_n_bc (conn,addr,i,j):

	if not i :
		conn.send("Hi " +chr(j+65)+" You are entering into the contest. The person who ll be first answering may only get the point(if one is correct)")
	else :
		conn.send("kk "+chr(j+65) + str(i))
	global answers
	answers=[]
	conn.send(que[i])
	while True :
		if len(answers)==i:
			ans=conn.recv(2048)
			broadcast(ans,conn,addr,0)
			answers.append(ans)
			score[ord(answers[i][0])-65]+=1
			for j in range(3):
				msg = "Score of "+chr(65+j) +" : "+ str(score[j]) 
				broadcast(msg,conn,addr,1)
			break
	return 





		
while(True):
	conn,addr=host.accept()
	contestants.append([chr(65+len(contestants)),conn,addr])
	if len(contestants)==3:
		for i in range(10):
			for j in range(3):
				thread.start_new_thread(recv_n_bc,(contestants[j][1],addr,i,j))




conn.close()
host.close()

