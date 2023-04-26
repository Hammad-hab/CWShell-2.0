import socket as s
from cli import highlighter
from threading import Thread
import subprocess as sb
import os, subprocess
from utilities import is_alive, observe_and_return_verb

# from interpreter import CWSHELL_INTERPRETER
class Socket():
    MX_BYTES = 1048576
    DEF_ENCODING = "utf-8"
    def __init__(self, *args, **kwargs) -> None:
        self.blacklist = []
    def send(self, msg) -> None:
        self.socket.send(bytes(str(msg), Socket.DEF_ENCODING))
        ...
    def kill(self, passive=False):
        if not passive:
            self.socket.close()
        else:
            return self.socket.close
    def murder(self):
        self.socket.close()
        del self
    
    def recive(self) -> bytes | str:
        msg = self.socket.recv(Socket.MX_BYTES)
        return msg.decode(Socket.DEF_ENCODING)
        ...
    @classmethod
    def make_from_connection(klass, conn):
        cls = klass()
        cls.socket = conn
        return cls
        ...
    @classmethod
    def make_socket(klass):
        socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        socket = klass.make_from_connection(socket)
        return socket
        ...
    
    def BlackList(self, addr : str):
        self.blacklist.append(addr)
        ...
        
    def accept(self):
        connection, addr = self.socket.accept()
        if addr[0] not in self.blacklist:
            connection = self.make_from_connection(connection)
            return connection, addr
        ...
    
    def connect(self, address, port):
        try :
            self.socket.connect((address,  int(port)))
        except Exception as e:
            self.kill()
            raise e
    
    def is_alive(self):
        return is_alive(self.socket)

    def is_dead(self):
        return not (is_alive(self.socket))
    
    def listen(self,address): 
        self.socket.bind(address)
        self.socket.listen()
    ...
    

class CWSH_INT:
    def __init__(self, socket, address) -> None:
        self.c_mode = "STD"
        self.modes = [
            "STD",
            "PYTHON",
            "BASH_RETURN",
            "BASH_NO_RETURN"
        ]
        self.socket = socket
        self.address = address
        self.mod_func = {}
        self._addModes()
    
    def _read(self, text):
        text = text.strip()
        if text[0: "switch".__len__()] == "switch":
            mode = text["switch".__len__():].strip()
            # self.c_mode = mode if len(mode) > 0 else "STD"
            if len(mode) > 0 and mode in self.modes:
                self.c_mode = mode
                print(highlighter.highlight(self.address[0] + " switched to "+ mode + " Mode"))
            elif len(mode) > 0 and mode not in self.modes:
                raise ValueError(f"BAD MODE {mode}")
            else:
                # modestr = '\n'.join(self.modes)
                self.c_mode = "STD"
                # print(f"Switched to STD (Standard) mode. Following are the available modes:{modestr}")
        else:
            return text
        ...
    
    def read(self, text):
        text = self._read(text)
        if text is not None:
            return self.mod_func[self.c_mode](text)
            ...
    
    def _addMode(self, mode_name):
        def function(func):
            if mode_name in self.modes:
                self.mod_func[mode_name] = func
            else:
                raise ValueError(f"unknown mode {mode_name}")
            ...
        return function
        ...
    
    def _addModes(self):
        # adding standard mode i.e “STD“
        @self._addMode("STD")
        def standard(text):
            print(
            highlighter.highlight(f"{self.address[0]} : {self.address[1]} {observe_and_return_verb(text)} {text}")
            )
            return "OK"

        @self._addMode("PYTHON")
        def python(text):
            try:
                 data = eval(compile(text, "<string>", "exec"))
            except Exception as e:
                return repr(e)
            else:
                return data
                
            ...
        @self._addMode("BASH_RETURN")
        def bash_r(text):
            try:
                highlighter.warn("Please note that the output of some functions might be sent to the server.")
                data = subprocess.check_output(text.split(" "), shell=True).decode()
            except Exception as e:
                return repr(e)
            else:
                return data if data.__len__() > 0 else "NO RETURN DATA"
                
            ...
        @self._addMode("BASH_NO_RETURN")
        def bash_r(text):
            try:
                data = os.system(text)
            except Exception as e:
                return repr(e)
            else:
                return "OK"
                
            ...
    ...