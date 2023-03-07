#!/usr/bin/python3
from cli import Map, Command, CommandEnviornment,CommandLoop, highlighter
from socket import gethostname
from utilities import GetIP
import os
from Socket import Server, Client
Environment = CommandEnviornment()
loop = CommandLoop(CommandEnviornment=Environment)

cname_map = Map("info")
cname_map.addParam(
"-i", "returns the ipaddress of the current machine", "--ip")
cname_map.addParam("-n", "returns the name of the current machine", "--name")

cname = Command(cname_map)

@cname.on("-i")
def ipv4(*args):
        ip = GetIP()
        return ip

...
@cname.on("-n")
def name(*args):
    name = gethostname()
    return name
...

exit_map = Map("exit")
exit_map.addParam("-f", "Forcefully exit the application", "--force")
exit_map.addParam("-r", f"restarts the application the application ({ highlighter.warn('WARNING: “exit -r“ is currently under development, it might duplicate operations',output=False) })", "--reload")
def delete():
    global Environment, loop
    del Environment
    loop.running = False
    del loop
    highlighter.warn('WARNING: “exit -r“ is currently under development, it might duplicate operations')
    os.system(f"./app.py")
    ...
Exit = Command(exit_map)
@Exit.on("-f")
def p(*args):
    exit()
@Exit.on("-r")
def r(*args):
    delete()


MAP = Map("server")
MAP.addParam("-a","the address to which the socket is to be bound. Enter the IP address then the port. Please note that the IP address must be the ipv4 of your machine, you can find your IPV4 using info -i", "--address") 
server = Command(MAP)



@server.on("-a")
def startServer(*args):
    s = Server(*args)
    s.start()
    
ClientM = Map("connect")
ClientM.addParam("-a", "The machines address, port and IP address to be percise. Example: connect -a <ipv4> <port>", "--address")
client = Command(ClientM)

@client.on("-a")
def connect(*args):
    cl = Client()
    # print(*args)
    cl.watch(args[0], int(args[1]))
    ...

Environment.add(cname, Exit,server, client)
# loop.start()