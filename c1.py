import socket
import pickle

s= socket.socket()
host = '127.0.0.1'
port = 5000
s.connect((host,port))
while (1):
    d = input("enter :")
    ds= pickle.dumps(d)
    s.sendall(ds)

s.close()
