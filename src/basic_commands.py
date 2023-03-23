from cli import Map, Command, highlighter
from socket import gethostname
from cli import Environment, loop
from utilities import GetIP
import os

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
    os.system("./app.py")
    ...
Exit = Command(exit_map)
@Exit.on("-f")
def p(*args):
    import sys
    sys.exit()
@Exit.on("-r")
def r(*args):
    delete()