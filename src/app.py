#!/usr/local/bin/python3
from commands import loop, highlighter
from utilities import Connected
if __name__ == "__main__":
    if Connected():
        loop.start()
    else:
        highlighter.warn("You are not connected to the internet, do you still want to  launch CWShell? Please note that various utilites might not work")
        d = input("[Y/N]? ")
        if d.strip().lower() == "y":
            loop.start()
        elif d.strip().lower() == "n":
            exit()
        else:
            highlighter.error("You must select either Yes [Y] or No [N]")
    