from random import random
from math import floor
import socket, ipaddress
import subprocess as sb

def search(entries):
    tried = []
    using = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        if tried.__len__() >= 100000:
            raise StopIteration("FAILED TO LOCATE AN UNUSED IP ADDRESS, ATTEMPTS EXCEEDED 100000")
        if entries == 1:
             d = f"192.168.43.{floor(random() * 500)}"
        elif entries == 2 :
            d = f"192.168.{floor(random() * 500)}.{floor(random() * 500)}"
        elif entries == 3:
            d = f"192.{floor(random() * 500)}.{floor(random() * 500)}.{floor(random() * 500)}"
        else:
            raise ValueError("The number of entry is too great")
        try:
            if d not in tried:
                using.bind((d,1040))
        except:
            tried.append(d)
        else:
            using.close()
            return d

def GetIP() -> str:
        from sys import platform
        if platform == "linux" or platform == "linux2":
            # linux 
            ...
        elif platform == "darwin":
            # OS X
            ip = sb.run(["ipconfig", "getifaddr", "en0"], capture_output=True)
            ...
        elif platform == "win32":
            # Windows...
            ip = sb.run(["ipconfig", "| findstr /i" "ipv4"],capture_output=True)
            ...
        return ip.stdout.decode().removesuffix("\n")

def Connected() -> bool:
    ip = GetIP()
    if ip.__len__() > 0:
        return True
    else:
        return False
    ...

def is_ipv4(ipv4 : str | bytes):
    try:
        IPV4 = ipaddress.ip_address(ipv4)
    except:
        return False
    else:
        return True
    ...