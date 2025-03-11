import socket
import pickle

s= socket.socket()
host = '127.0.0.1'
port = 5000
s.connect((host,port))
d = input("enter b :")
ds= pickle.dumps(d)
s.sendall(ds)


s.close()