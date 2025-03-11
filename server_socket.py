import socket
import pickle
import threading

def recvd_data(con):
    while True:
        data = con.recv(1024) #waiting call
        desearilize_data = pickle.loads(data)
        print("Data received =>", desearilize_data)
        r = len(desearilize_data)
        print(r)
        
        
        

x=socket.socket()
host = '127.0.0.1'
port = 5000
x.bind((host,port))

x.listen(5) #waiting call
con, addr = x.accept()
print("Client Connected")
li=[]
for i in range(2):
    t=threading.Thread(target=recvd_data, args=(con,))
    t.start()
    li.append(t)
    print("main scope is running")
for i in li:
    i.join()
x.close()