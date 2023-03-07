import socket as s
from cli import highlighter
from threading import Thread
import subprocess as sb
import os
from utilities import is_alive
from interpreter import CWSHELL_INTERPRETER
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
        self.modes = ["PYTHON", "BASH_NO_RETURN", "BASH_RETURN", "STD"]
        self.mode = "STD"
        self._emergency_abort = False
        self.clients: list[Thread] = []
    def handleClient(self, conn, addr, server):
        conn.send(bytes(f"{server[0]}:{s.gethostname()}", "utf-8"))
        print(highlighter.highlight(f"{addr[0]} : {addr[1]} connected"))
        ended = False
        while self.running:
            try:
              if self._emergency_abort:
                    conn.close()
                    exit()
              else:
                c: str = conn.recv(self.MX_BYTES).decode()
                if "§" in c:
                    c = c.replace("§", "")
                csp = c.split(" ")

                if c == "end":
                     print(
                     highlighter.highlight(f"{addr[0]} disconnected")
                     )
                     conn.send("OK".encode())   
                     conn.close()
                     break
                elif csp[0].strip() == "switch":
                    if csp[1].upper().strip() in self.modes:
                        self.mode = csp[1]
                    else:
                        conn.send(b"NOT VALID MODE")
                    ...
                else:
                    if c.strip().__len__() != 0:
                        if self.mode == "STD":
                            print(highlighter.highlight(f"{addr[0]} : {addr[1]} said {c}"))
                        elif self.mode == "BASH_NO_RETURN":
                            os.system(c)
                        elif self.mode == "BASH_RETURN":
                            output = sb.run(c, capture_output=True)
                            conn.send(output.stdout)
                        elif self.mode == "PYTHON":
                            rt = exec(c)
                            conn.send(bytes(rt, "utf-8"))
                    
                conn.send(b"OK")
            except Exception:
                break
    def start(self):
        ...
        try:
            IP = self.args[0].strip()
            PORT = int(self.args[1].strip())
            ADDR = (IP, PORT)
            self.socket.bind((IP, PORT))
            self.socket.listen()
            while self.running:
                try:
                    connection, address = self.socket.accept()
                    client = Thread(target=self.handleClient,args=(connection, address, ADDR))
                    client.start()
                    self.clients.append(client)
                except KeyboardInterrupt:
                    raise Exception
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
            while self.running and is_alive(self.socket): 
                try:
                    if is_alive(self.socket):
                        data = input(f"{machine_name} $ ")
                        # self.socket.send(data.encode())
                        
                        function = CWSHELL_INTERPRETER.see(data)
                        if function is not False:
                            function(self.socket)
                        else:
                            self.socket.send(data.encode())
                            rdata = self.socket.recv(1024).decode()
                            print(rdata)
                            
                    else:
                        raise Exception("SERVER CLOSED CONNECTION")

                except KeyboardInterrupt:
                    highlighter.error("KeyboardInterrupt! Input was not recorded")
                    # exit()
                    ...
                ...
            return 
        except Exception as e:
            self.socket.send(b"end")
            highlighter.error(f"{e!r}", True)
        ...