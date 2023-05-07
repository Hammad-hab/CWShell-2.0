import os
import subprocess
class CWSH_LANG:
    def __init__(self) -> None:
        self.Commands = {
            "cd":         self._cwshlang_create_function(os.chdir, 1),
            "ls":         self._cwshlang_create_forgiving_func(os.listdir),
            "mkdir":      self._cwshlang_create_function(os.mkdir, 1),
            "chmod":      self._cwshlang_create_function(os.chmod, 2),
            "pwd":        self._cwshlang_create_function(os.getcwd, 0),
            "cat":        self._cwshlang_create_function(self._cat_implementation, 1),
            "echo":       self._cwshlang_create_forgiving_func(print),
            "clear":      self._cwshlang_create_forgiving_func(lambda: os.system("clear")),
            "cp":         self._cwshlang_create_function(self._copy_implementation, 2),
            "run_dormat": self._cwshlang_create_forgiving_func(lambda args: os.system(" ".join(args)))
        }

        pass

    def parse(self, input: str | bytes):
        command = input.split(" ")
        command = (command[0], command[1:])
        command_name, command_args = command
        for name, executor in self.Commands.items():
            if name == command_name:
                return executor(*command_args)
            ...
        raise ValueError(
            f"Command {command_name} is not defined in the env dictonary")
        ...

    def _cwshlang_create_function(self, func, number_args: int):
        if type(number_args) != int:
            raise ValueError(
                f"expected the number_args to be int but recived type {type(number_args)}")
            ...
        _FUNC = lambda *args: self._cwshlang_create_function_func(
            number_args, func, *args)
        return _FUNC

    def _cwshlang_create_forgiving_func(self, func):
        _FUNC = lambda *args: self._cwshlang_create_function_func(
            args.__len__(), func, *args)
        return _FUNC
        ...

    def _cwshlang_create_function_func(self, expc, func, *args):
        number_expected = expc
        function = func
        args = args
        if args.__len__() != number_expected:
            raise ValueError(
                f"Function {func.__name__} expected {number_expected} { 'arguments' if number_expected > 1 else 'argument'} but recived {args.__len__()} instead")
        return function(*args)
        ...

    def _cwshlang_testing_repl(self):
        while True:
            inp = input(">>> ")
            print(self.parse(inp))
        ...

    def _cat_implementation(*args: list[str]):
        with open(args[1], "r+") as f:
            lines = f.read()
            # for line in lines:
            return lines
    def _copy_implementation(*args: list[str]):
        print(args)
        file:str = args[1]
        newPath: str = args[2]
        
        _PROCESS = subprocess.Popen(["cp", file, newPath])
        return _PROCESS.stdout
    ...