from random import random
from math import floor
import socket
import ipaddress
import subprocess as sb
import os
from rich.console import Console
import readline
import subprocess

console = Console()
initial_input = input
def search(entries):
    tried = []
    using = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        if tried.__len__() >= 100000:
            raise StopIteration(
                "FAILED TO LOCATE AN UNUSED IP ADDRESS, ATTEMPTS EXCEEDED 100000")
        if entries == 1:
            d = f"192.168.43.{floor(random() * 500)}"
        elif entries == 2:
            d = f"192.168.{floor(random() * 500)}.{floor(random() * 500)}"
        elif entries == 3:
            d = f"192.{floor(random() * 500)}.{floor(random() * 500)}.{floor(random() * 500)}"
        else:
            raise ValueError("The number of entry is too great")
        try:
            if d not in tried:
                using.bind((d, 1040))
        except:
            tried.append(d)
        else:
            using.close()
            return d


def GetIP() -> str:
    if getOS() == "Linux":
        # linux
        ...
    elif getOS() == "MacOS":
        # OS X
        ip = sb.run(["ipconfig", "getifaddr", "en0"], capture_output=True)
        ...
    elif getOS() == "Windows":
        # Windows...
        ip = sb.run(["ipconfig", "| findstr /i" "ipv4"], capture_output=True)
        ...
    return ip.stdout.decode().removesuffix("\n")


def getOS():
    from sys import platform
    if platform == "linux" or platform == "linux2":
        return "Linux"
        ...
    elif platform == "darwin":
        # OS X
        return "MacOS"
    elif platform == "win32":
        # Windows...
        return "Windows"
        ...


def Connected() -> bool:
    ip = GetIP()
    if ip.__len__() > 0:
        return True
    else:
        return False
    ...


def is_ipv4(ipv4: str | bytes):
    try:
        IPV4 = ipaddress.ip_address(ipv4)
    except:
        return False
    else:
        return True
    ...


def is_alive(socket: socket.socket):
    prepStr = "§§§".encode()
    try:
        socket.send(prepStr)
    except:
        return False
    else:
        return True
    # ...


def locate_file(filename):
    print("FOR OPEN-SOURCE ONLY")
    os.chdir("/")
    LIST = os.listdir()


def observe_and_return_verb(sentence: str):
    """
    This is a really exotic and funny function. It basically searches for certain symbols in the clients messages and then returns the
    verb that should describe it. Its implementation isn't that complex, just an if condition checking for exclamation marks, question 
    marks et cetera. A combination of symbols i.e "?!" could lead to other outputs such as "urgently inquires", you see, it's really 
    interesting. This is where the fun part drops in: if you send text based emojis i.e :), :(, it adds the name of the emotion and
    then adds the verb "says". The emojis it currently supports are as follows:
     _____________________________________________________________________
    |  Emoji  |    Name    |                    Output                    |
    |_________|____________|______________________________________________|
    |  :)     |Smily face  |  <ipaddress>:<port> smiles and says <message>|
    |  :(     |Sad   face  |  <ipaddress>:<port> sobs and says <message>  |
    |  >:(    |angry face  |  <ipaddress>:<port> frowns and says <message>|
    |  ;(     |winking face|  <ipaddress>:<port> winks and says <message> |
    |  ~_~    |crying face |  <ipaddress>:<port> crys and says <message>  |
    |_________|____________|______________________________________________|
    """
    

    SYMB = {
        "?!": "shouts and asks",
        "!?": "urgently inquires",
        "??": "inquires",
        "?": "asks",
        "!": "exclaims",
        ">:(": "frowns and says",
        ":(": "sobs and says",
        ":)": "smiles and says",
        ";)": "winks and says",
        "~_~": "crys and says"
    }
    for symb, description in SYMB.items():
        if symb in sentence:
            return description
    return "says"
    ...


def install_packages():
    """ 
    This command was not used in the CWSHELL code. It is a utility made for open-source users so that they can download all the 
    packages with convienience and so that they do not have to download every package manually. To use this command, navigate 
    to the src directory and then enter the REPL by typing “python3“. After entering the REPL, run “from utlitilies import 
    install_packages“ and then execute the command.
    NOTE:
    Make sure you are in the source directory because the src directory is not in the sys.path list and because 
    this command needs the “requirements.txt“ to function.
    """
    items = os.listdir()
    if "requirements.txt" not in items:
        raise FileNotFoundError("This function needs requirments.txt to work. You might have deleted the file, if not, then install the software source again or get another copy of \
            requirements.txt from the github repo.")
    else:
        with open("requirements.txt", "r") as f:
            lines = f.readlines()
            OS = getOS()

            for line in lines:
                if len(line.strip()) == 0:
                    continue
                if OS == "MacOS" or OS == "Linux":
                    os.system(f"pip install {line}")
                    return 1
                elif OS == "Windows":
                    print("This command may or may not work on windows depending on whether the pip executable in in the enviornment variables or not. Please ensure that before continuing")
                    input("Press enter to continue")
                    os.system(f"pip install {line}")
                    return 0

            raise ValueError(
                "THE FILE REQUIRMENTS.TXT IS EMPTY. REVIVE THE CONTENTS OR ATTAIN A NEW COPY OF THE FILE FROM THE GITHUB REPO")

            ...
    ...

def compile(*, onefile=True):
    """
    This command wasn't used in the CWSHELL code. It is a utility function made for open-source users so that
    they can compile the file with ease. Following are the steps to use this command:
    ⚪️ Naviagte to the CWSHELL source directory
    ⚪️ Enter the python repl by typing “python3“ (or “python“ if you are using python 2)
    ⚪️ Import this function from the repl by executing “from utilities import install_packages, compile“
    ⚪️ First execute the function install_packages (READ THE INSTRUCTIONS OF “install_packages“. 
                                                    In the repl you can do that by executing 
                                                    help(install_packages))
    ⚪️ Then execute the compile function and wait. The function will generate a dist folder and within the dist folder
    will be your executable. Happy remote controlling!
    
    NOTE: This function is using pyinstaller.
    """
    process = subprocess.Popen(["pyinstaller", "--onefile" if onefile is True else "", "app.py"])
    # if process.stdout:
    os.rmdir("build")
    os.remove("./app.spec")
    # exit()
    ...

def input(str):
    text = initial_input(str)
    readline.add_history(text)
    
    return text
    ...
    
