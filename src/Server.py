from cli import Map, Command, highlighter
from Socket import Socket, CWSH_INT
from threading import Thread
class Server:
    def __init__(self, address, port) -> None:
        self.sk = Socket.make_socket()
        self.running = True
        self.addr = (address, int(port))
        self.clients: list[dict] = []
        # self.INT = 
        
    def handleClient(self, conn: Socket, addr: tuple[str | bytes | int]): 
        INT = CWSH_INT(self.sk, self.addr)
        while self.running and conn.is_alive():
            try:
                data = conn.recive()
                data = data.replace("§", "")
                if data == "END":
                    conn.kill()
                    return None
                if data:
                    return_data = INT.read(data)
                    conn.send(return_data)
                else:
                    return_data = ""
            except Exception as e:
                highlighter.error(f"An error occured. {e}")

        return return_data
        ...
    
    def print(self, addr):
        print(
        highlighter.highlight(f"{addr[0]} : {addr[1]} connected")           
        )
    
    def _newClientThread(self, connection, address):
        THREAD = Thread(target=self.handleClient, args=(connection, address))
        CLIENT = {
            "socket": connection,
            "address": address,
            "thread": THREAD
        }
        # THREAD.kill
        THREAD.start()
        self.clients.append(CLIENT)
        return THREAD
        ...

    def start(self):
            try:
                self.sk.listen(self.addr)
                while self.running:
                    try:
                        conn, addr = self.sk.accept()
                        self.print(addr)
                        self._newClientThread(conn, addr)
                    except Exception:
                        self.sk.kill()
                        raise
            except Exception as e:
                self.sk.kill()
                raise
            ...      
    

MAP = Map("server")
MAP.addParam("-a","the address to which the socket is to be bound. Enter the IP address then the port. Please note that the IP address must be the ipv4 of your machine, you can find your IPV4 using info -i", "--address") 
server = Command(MAP)

@server.on("-a")
def startServer(*args):
    s = Server(*args)
    s.start()