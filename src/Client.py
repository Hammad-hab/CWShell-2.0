from Socket import Socket
from cli import Map, Command, highlighter
from utilities import console, input

class Client:
    def __init__(self, address, port) -> None:
        self.sk = Socket.make_socket()
        self.addr = (address, port)
        self.sk.connect(address, port)
        # if self.sk.is_alive():
        self._loop()
            
    def _loop(self):
        while self.sk.is_alive():
            try:
                # print(self.sk.is_alive())
                data = input(f"{self.addr[0]} $ ")
                if data == "exit":
                    self.sk.send("END")
                    self.sk.kill()
                else:   
                    self.sk.send(data)
                    Data = self.sk.recive()
                    Data = Data.replace("§", "")
                    console.print(Data)
            except:
                ...
            
            ...
        highlighter.error("SESSION ENDED")
                

ClientM = Map("connect")
ClientM.addParam("-a", "The machines address, port and IP address to be percise. Example: connect -a <ipv4> <port>", "--address")
client = Command(ClientM)

@client.on("-a")
def connect(*args):
    cl = Client(*args)
    ...