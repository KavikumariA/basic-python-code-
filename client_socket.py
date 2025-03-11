import socket
import pickle

x=socket.socket()
host = '127.0.0.1'
port = 5000
x.connect((host,port))
while True:
    data = input("Enter your message : ")
    searilze_data = pickle.dumps(data)
    x.sendall(searilze_data)
x.close()