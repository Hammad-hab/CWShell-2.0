import socket as s
from utilities import GetIP
ADDR = ("192.168.43.50", 1341)
Socket = s.socket(s.AF_INET, s.SOCK_STREAM)
Socket.connect(ADDR)
print(Socket.recv(1024))
Socket.send(f"{s.gethostname()}:{GetIP()}")