import socket
import pickle
import threading
s = socket.socket()
host = '127.0.0.1'
port = 5000
s.bind((host,port))
s.listen(5)
p = 0
def dd(c):
    
    data =c.recv(1250)
    data = pickle.loads(data)
    print(data)

while p<=2:
    c,a = s.accept()
    print("connected")
    dd(c)
    p=p+1


lis =[]

for i in lis:
    t = threading.Thread(target ="dd", args=(i))
    
    t.start()
    


for i in lis:
    i.join()



c.close()


