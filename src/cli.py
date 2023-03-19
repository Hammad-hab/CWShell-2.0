"""
Example:

print_m =  Map("help")
print_m.addParam("-pr", "prints raw strings")
print_m.addParam("-p", "prints f-strings, byte-strings and every other type of strings, inculding raw strings", "--print")

Print = Command(print_m)
@Print.on("-p")
def log(*args):
    print(*args)
    
Print.run("-p","Hello World!")
"""
from termcolor import colored
import keyword, sys
from utilities import is_ipv4, getOS

def try_ignore(function, *args, **kwargs):
    try:
        return function(*args, **kwargs)
    except:
        return None
    ...

class Map:
    def __init__(self, cmd_name) -> None:
        """
        Map class is a info blueprint that contains information about the command, the commands name, its parameters et cetra
        Arguments:
            cmd_name: the name of the command
        Example:
            print_m = Map("print")
            print_m.addParam("-pr", "prints raw strings")
            print_m.addParam("-p", "prints f-strings, byte-strings and every other type of strings, inculding raw strings", "--print")
        """
        self.command = cmd_name
        self.base_str = f"usage {self.command}:"
        self.attribs = {
        }
    def addParam(self, param_name, description, param_long=None):
        """
        This method adds information about a commands parameter. 
        Arguments:
            param_name: the name of the parameter
            description: the description that is to be displayed when "help" is executed
            param_long [optional]: it is the long name of the parameter, for example the long name of "-ls" is "--list".
        Example:
            print_m.addParam("-pr", "prints raw strings")
            print_m.addParam("-p", "prints f-strings, byte-strings and every other type of strings, inculding raw strings", "--print")
        """
        self.attribs[param_name] = {
            "description": description,
            "long_parameter": param_long
        }
        self.base_str += f"\n\t{param_name} {f'[{param_long}]' if param_long is not None else ''}: {description}"
        ...

class Command:
    def __init__(self, command_info: Map) -> None:
        """
        The class used for creating commands. To create a command you need its information which is genereated by the 
        Map class. 
        Each command has a "-h" ("--help") command by default.
        
        Arguments:
            command_info: the information of the command i.e class Map
        Example:
        Print = Command(print)
        @Print.on("-p")
        def log(*args):
            print(*args)
        """
        self.name = command_info.command
        self.parameters = command_info.attribs
        self.__help__ = command_info.base_str
        
        pass

    def help(self):
        print(self.__help__)
        ...

    def on(self, param):
        """
        The "on" method is a decorator that binds a function to the given parameter
        Arguements:
            param: the name of the parameter to which a function is to be bound. IT CURRENTLY DOES NOT SUPPORT LONG_PARAMETER NAMES
        Example:
            @print.on("-p")
            def log(*args):
                print(*args) // *args are the arguments that were passed when the function was called
        """
        if param not in self.parameters.keys():
            raise ParameterNotFound(
                "Undefined Parameter {}.".format(param))

        def decorator(f):
            self.parameters[param]["function"] = f
            ...
        return decorator
        ...

    def __run__(self, parameter, *args):
        parameter = parameter.strip()
        """
        Runs the function with the provided arguments. 
        Arguments:
            parameter: The name of the parameter to which the next value is assigned
            value: The argument to pass into the function when it is executed.
        Example:
            Print.run("-p", "Hello World!")
        """
        try:
            return self.parameters[parameter]["function"](*args)
        except KeyError as e:
           for param_n, paramobj in self.parameters.items():
               name = paramobj["long_parameter"]
               if parameter == name:
                   returnV = self.parameters[param_n]["function"](*args)
                   return returnV
               elif parameter == "-h" or parameter == "--help":
                   return self.help()

               else:
                   continue
           raise ParameterNotFound(e.args)
        ...

class CommandEnviornment:
    def __init__(self) -> None:
        self.commands: dict[Command] = {}
        self.spec_var = {
            "$LAST_OUTPUT": "None"
        }
        pass
    def add(self, command: Command, *commands) :
            self.commands[command.name] = command
            if commands.__len__()  > 0:
                for c in commands:
                     self.commands[c.name] = c

    def getFromUnixStyle(self, unix: str):
        # for spc_var, value in self.spec_var.items():
        #     unix = unix.replace(spc_var, value)
        
        command = unix.split(" ")
        command = [x.strip() for x in command]
        name = command[0].strip()
        params = command[1:]
        params = [x.strip() for x in params if x.__len__() > 0]
        return (name, params)
        ...
    def help(self):
        Help = ""
        for name, command in self.commands.items():
              h = command.help()
              Help += (h if h is not None else "")
        return Help
        ...
    def findrun(self, name: str, *params):
             return self.commands[name].__run__(*params)
    ...


class CommandLoop:
    def __init__(self, *, CommandEnviornment: CommandEnviornment, prompt=">>> ", autorun=False) -> None:
        self.welcomePrompt = f"CWShell v2.0. Application is using PythonV{sys.version[0: sys.version.index('(') - 1]}. Type “help“ to get more info" 
        self.prompt = prompt
        self.running = True
        self.highlighter = SyntaxHighlighter()
        self.env = CommandEnviornment
        self.error = {}
        self.prev = ""
        if autorun:
            self.start()
        pass
 
    
    def on_error(self, error):
       def f(function):
            self.error[error] = function     
       return f
    def g_exception(self, e: Exception):
        nm = repr(e)
        nm = nm[0: nm.index("(")]
        return str(nm)
        ...
    
    def start(self):
        print(self.welcomePrompt)
        while self.running:
            try:
                data = input(self.prompt).strip()
                if data.strip().__len__() > 0:
                    fdata = list(self.env.getFromUnixStyle(data))
                    if fdata[0].lower().strip() == "help":
                        self.env.help()
                        continue
                        ...
                    elif fdata[0].lower().strip() == "clear":
                        if getOS() == "Linux" or getOS() == "MacOS":
                            __import__("os").system("clear")
                        else:
                            __import__("os").system("cls")
                            
                            
                    else:
                        if fdata[1].__len__() < 1:
                            fdata[1] = ["-h"]
                            ...
                        try:
                            returnV = self.env.findrun(fdata[0], *fdata[1])
                        except Exception as e:
                            try_ignore(lambda e: self.error[self.g_exception(e)](e), e)
                            self.highlighter.error(f"{e!r}", fancy=True)
                            # raise
                        else:
                            if returnV:
                                print(returnV)
                            self.prev = data
                        
            except KeyboardInterrupt as e:
                self.highlighter.error(f"\n{e!r} input not recorded", fancy=True)
                pass
        ...

    ...
    
class ParameterNotFound(KeyError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    ...

class SyntaxHighlighter:
    def __init__(self) -> None:
        pass
    def highlight(self,strn:str):
        arr = strn.split(" ")
        
        for element in arr:
            if keyword.iskeyword(element):
                index = arr.index(element)
                arr[index] = colored(element, "magenta",attrs=["bold"])
            elif element.isdigit() or element.isdecimal() or is_ipv4(element):
                index = arr.index(element)
                arr[index] = colored(element, "green",attrs=["bold"])
            elif element.isalpha():
                index = arr.index(element)
                arr[index] = colored(element, "blue",attrs=["bold"])
        return "".join([x + " " for x in arr])
    def error(self, string:str, fancy=False, output=True):
        colorString = self._stdout(string, "red", fancy, output)
        return colorString
        ...
    def _stdout(self, string, color, fancy=False, output=True):
        colorString = colored(string, color, None if fancy is False else f"on_{color}",attrs=["bold"])
        if output is True:
            print(colorString)
        return colorString 
        ...
    
    def warn(self, string:str, fancy=False, output=True):
        colorString = self._stdout(string,"yellow",fancy, output)
        return colorString
    
    ...
highlighter = SyntaxHighlighter()

Environment = CommandEnviornment()
loop = CommandLoop(CommandEnviornment=Environment, prompt="🐚 ")