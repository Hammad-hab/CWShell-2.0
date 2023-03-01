import socket as s
from cli import highlighter
from threading import Thread

class Socket():
    def send(self, msg):
        self.socket.send(bytes(msg, "utf-8"))
        ...
    def recive(self):
        msg = self.socket.recv(102313)
        return msg.decode("utf-8")
        ...
    ...

class Server(Socket):
    def __init__(self, *args) -> None:
        super().__init__()
        self.socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.args = args
    def handleClient(self, conn, addr, server):
        conn.send(bytes(f"You connected to {server[0]}", "utf-8"))
        print(f"{repr(addr)} connected")
        msg = conn.recv(1024)
        
    def start(self):
        ...
        try:
            IP = self.args[0].strip()
            PORT = int(self.args[1].strip())
            ADDR = (IP, PORT)
            self.socket.bind((IP, PORT))
            self.socket.listen()
            while True:
                connection, address = self.socket.accept()
                client = Thread(target=self.handleClient,args=(connection, address, ADDR))
                client.start()
                ...
        except Exception as e:
            self.socket.close()
            print("Connection closed due to error")
            highlighter.error(f"{e!r}",True)
    ...

class Client(Socket):
    def __init__(self) -> None:
        super().__init__()
        self.socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    def watch(self, address: str, port: int):
        self.socket.connect((address, port))
        
        ...