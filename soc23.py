import socket
import pickle
import threading


def dd(i):
    
    w = i.recv(1000)
    w = pickle.loads(w)
    print(w)
    s.send(w)

s = socket.socket()

host = '127.0.0.1'
port = 5000
s.bind((host,port))

s.listen(1)
client=[]
for i in range (1):
    con,adr = s.accept()
    client.append((con,adr))
    print("Client connected")
r=[]
for i in client:
    t=threading.Thread(target=dd, args=(i))
    t.start()
 


s.close()




