import socket as s
from cli import highlighter
from threading import Thread
import subprocess as sb
import os
class Socket():
    MX_BYTES = 1048576
    DEF_ENCODING = "utf-8"
    def send(self, msg) -> None:
        self.socket.send(bytes(msg, Socket.DEF_ENCODING))
        ...
    def recive(self) -> bytes | str:
        msg = self.socket.recv(Socket.MX_BYTES)
        return msg.decode(Socket.DEF_ENCODING)
        ...
    ...

class Server(Socket):
    def __init__(self, *args) -> None:
        super().__init__()
        self.socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.args = args
        self.running = True
        self._emergency_abort = False
        self.clients: list[Thread] = []
    def handleClient(self, conn, addr, server):
        conn.send(bytes(f"{server[0]}:{s.gethostname()}", "utf-8"))
        print(highlighter.highlight(f"{addr[0]} : {addr[1]} connected"))
        ended = False
        while self.running:
              if self._emergency_abort:
                  conn.send("end".encode())
                  conn.close()
                  ended = True
                  
                  exit()
            #   if not ended:
              c = conn.recv(self.MX_BYTES).decode("utf-8")
              print()
              if c == "end" and not ended:
                  conn.send("OK".encode())
                  conn.close()
                  ended = True
              c_a = c.split(" ")
              try:
                s_ = sb.run(c_a,capture_output=True)
              except Exception as e:
                  if not ended:
                      conn.send(f"Error {e!r}".encode())
                      break
              else:   
                if s_.stdout.decode().strip() == "":
                   s_.stdout = b"Failed to attain output"
                #    print(True)
                conn.send(s_.stdout)
    def start(self):
        ...
        try:
            IP = self.args[0].strip()
            PORT = int(self.args[1].strip())
            ADDR = (IP, PORT)
            self.socket.bind((IP, PORT))
            self.socket.listen()
            while self.running:
                connection, address = self.socket.accept()
                client = Thread(target=self.handleClient,args=(connection, address, ADDR))
                client.start()
                self.clients.append(client)
                ...
        except Exception as e:
            self._emergency_abort = True
            self.running = False
            self.socket.close()
            highlighter.error("Connection closed due to error")
            highlighter.error(f"{e!r}",True)
    ...

class Client(Socket):
    
    def __init__(self) -> None:
        super().__init__()
        self.socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.running = True
    def watch(self, address: str, port: int):
        try:
            self.socket.connect((address, port))
            machine_data = self.recive().split(":")
            # print(machine_data)
            machine_name = machine_data[1]
            machine_local_ipv4 = machine_data[0]
            while self.running: 
                try:
                    data = input(f"{machine_name} $ ")
                    if data == "clear":
                        os.system("clear")
                    elif data == "exit":
                        self.send("end")
                        msg= self.recive()
                        if msg == "OK":
                            exit()
                    self.send(data.strip())
                    data = self.recive()
                    if data == "end":
                        self.socket.close()
                        highlighter.error("Server ended session")
                        break
                    else :
                        print(data)
                except KeyboardInterrupt:
                    print("")
                    ...
                ...
            return 
        except Exception as e:
            highlighter.error("Error occured soo deep in the application that we can't display it : (", True)
        ...