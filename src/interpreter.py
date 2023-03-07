import os
import sys
class CWSH_INT:
    def __init__(self) -> None:
        self.commands: dict = {}
        pass
    def add(self, name: str):
        def decorator(function):
            self.commands[name] = function
            ...
        return decorator
        ...
    def see(self, input: str | bytes):
        for n, v in self.commands.items():
            # print(n)
            if input.strip() == n.strip():
                return self.commands[n]
            else:
                continue
        return False
        ...
    
CWSHELL_INTERPRETER = CWSH_INT()
@CWSHELL_INTERPRETER.add("end")
def end(*args):
    # data = args[0]
    socket = args[0]
    socket.send(b"end")
    rdata = socket.recv(1024).decode()
    exit()
    ...
    
@CWSHELL_INTERPRETER.add("clear")
def clear(*args):
    if sys.platform == "darwin" or sys.platform == "linux" or sys.platform == "linux2":
        os.system("clear")
    else: 
        os.system("cls")
