from rich.markdown import Markdown
# As you might have precived, these long string are printed whenever the “whats_new“ command is called.
# Altering them will result in the alteration of the output of the “whats_new“ command. Tinkering with
# this is not at all appreiciated even though the application won't break!
UPDATE_V2_1_BREIF = "Added new mode CWSH. Removed modes: BASH_RETURN, BASH_NO_RETURN, PYTHON"

UPDATE_V2_1_LONG = """
## Removals
The modes that were release as early access are henceforth removed from the CWShell source.
The BASH_RETURN mode was removed because it was too dependent on the subprocess module that 
often sent the output to the server instead of the client. 
The BASH_NO_RETURN mode was removed because it's uselessness. The BASH_NO_RETURN was instructed 
to either remove the output altogether or send the output to the server instead of the client 
which seemed quite absurd. Another problem with the BASH_RETURN and the BASH_NO_RETURN was that 
they were unable to change directories permenantly. Whenever the cd command was executed, the 
directory did not change. This was because the subprocess module spawned an entire new process f
or each and every command. Therefore the directory did change for one process but did not for the 
others. *This problem has been solved in 2.1 (More about this in CWSH section)*
The PYTHON mode was removed because it was sacrificing major python abilites due to the usage of 
eval, compile and exec functions. This mode was not at all useless and we might as well add a more 
reliable implementation of this mode in future versions.

## CWSH, new beginnings
In exchange for all these modes we offer the CWSH mode that solves almost all the problems of the above mentioned 
modes. The CWSH does not rely on the subprocess module and instead uses a custom-built BASH/ShellScript executor 
called CWSHLang. CWSHLang (If you are using the source you can find the class implementation in CWSHLang.py) is a
mini-executor that ensures the availbility of the output. Frankly speaking, it makes use of the os module and 
directs the entered command's name and arguments to os module's repective function. Unfortunatly CWSH only supports
a selective few of the essential BASH commands such as cd, ls, mkdir et cetera. Creating a fully-fledged executor 
was beyond the scope of this release. 
For now we have a special command called `run_dormat` in CWSH mode that uses the functionality of BASH_NO_RETURN mode 
and can be used to execute other functions that are currently not supported (example: ps -A, arp and ifconfig).
Following list of commands that are supported:
⚪️ mkdir
⚪️ cd
⚪️ ls
⚪️ chmod
⚪️ echo (renders the result on your screen, not on the servers. This command uses the print function to achive this.)
⚪️ clear
"""

