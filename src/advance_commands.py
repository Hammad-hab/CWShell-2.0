from cli import Map, Command, highlighter
import os
from cli import Environment, loop
from rich.console import Console
console = Console()
execute_fm_map = Map("exec_from")

execute_fm_map.addParam(
    "-f", """This parameter should be the name of the file. Basically this command is used to run cwshell commands that were written into a file, 
    kind of like Shellscript. Syntax: exec_from -f <filename>. 
    This is one of the advance commands of CWShell so please be sure to read the documentation.
    """, "--file")

execute_fm_map.addParam(
    "-p", """This parameter is not very useful but you can still use it in your file.cwsh. 
    In a nutshell, this command prints whatever you give it, file, string, variable etc.
    """,
    "--print"
)


execute_fm = Command(execute_fm_map)
@execute_fm.on("-f")
def from_file(*args):
    filename = args[0]
    if os.path.isfile(filename):
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                d = Environment.getFromUnixStyle(line)
                ret = Environment.findrun(d[0], *d[1])
                print(ret)
            ...
        
    else:
        highlighter.error(f"{filename} is not a file!")

@execute_fm.on("-p")
def from_none_print(*args):
    print_d = args[0]
    if os.path.isfile(print_d):
        with open(print_d) as f:
            print(f.read())
        ...
    else:
        print(print_d)
         
    ...
    
wh_new_map = Map("whats_new")
wh_new_map.addParam("-b", "Explains the updates breifly", "--breif")
wh_new_map.addParam("-d", "Explains the updates in detail", "--detail")

wh_new = Command(wh_new_map)
@wh_new.on("-b")
def breif():
    from __updates__ import UPDATE_V2_1_BREIF
    console.print(UPDATE_V2_1_BREIF)
    ...
    
@wh_new.on("-d")
def detailed():
    from __updates__ import UPDATE_V2_1_LONG

    console.print(UPDATE_V2_1_LONG)
    ...