import socket
import pickle

y= socket.socket()
host = '127.0.0.1'
port = 5000
y.connect((host,port))
d = input("enter a :")
ds= pickle.dumps(d)
y.sendall(ds)


y.close()