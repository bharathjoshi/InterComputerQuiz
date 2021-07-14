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

def recv_n_bc (conn,addr):

	conn.send("Hi " +chr(len(contestants)+64)+" You are entering into the contest. The person who ll be first answering may only get the point(if one is correct)")
	global var 
	var=0
	for k in range(3):
		print k

		while True :

			if len(contestants)!=3:
				global answers 
				answers=[]
			if len(contestants)==3  and len(answers)==k: 
				if  not k:
					conn.send("Starting game nibbas")
				else :
					conn.send("Question " + str(k+1))
				conn.send(str(que[k]))
				while var==k:
					ans = conn.recv(2048)
					if ans :
						var+=1
				print ans
				print "k==="+ str(k)
				if len(answers)==k:

					broadcast(ans,conn,addr,0)
					answers.append(ans)
				score[ord(answers[k][0])-65]+=1
				if len(answers)==k+1:
					print answers
					for i in range(3):
						msg = "Score of "+chr(65+i) +" : "+ str(score[i]) 
						broadcast(msg,conn,addr,1)
					break



		
while(True):
	conn,addr=host.accept()
	contestants.append([chr(65+len(contestants)),conn,addr])
	#print("1"  +  chr(65+len(contestants)) )


	#print(addr[0]+" connected")
	thread.start_new_thread(recv_n_bc,(conn,addr))
	#print(len(contestants))
	#print("2"  +  chr(65+len(contestants)) )


conn.close()
host.close()

