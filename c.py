import socket
import pickle
s = socket.socket()
host = '127.0.0.1'
port = 5000
s.connect((host, port))
# while (1):
#     s1 = input("enter the value")
#     data = pickle.dumps(s1)
#     s.sendall(data)
# s.close()
