#!/usr/bin/env python3

import re

class options:
    def __init__(self, shortargs: list, longargs: list, gotargs: list, compulsory_short_args:list[str] = [], compulsory_long_args:list[str] = []):
        """init function: This runs everytime the class is called.

        Args:
            shortargs (list): example: ['h', 'l', 'i', ...]
            longargs (list): example: ['help', 'lock', 'init', ...]
            gotargs (list): sys.argv[1:]
            compulsory (list | optional): compulsory args
        """
        self._args = gotargs
        self._shortargs = shortargs
        self._longargs = longargs
        self._compulsory_short = compulsory_short_args
        self._compulsory_long = compulsory_long_args
        self._gotargs = []
        self._argcheck = True
        self._argerror = 'no error'
        self._falseargs = []

        # add '-' to the front of the args
        for i in range(len(self._shortargs)):
            self._shortargs[i] = '-' + self._shortargs[i]
        
        for i in range(len(self._longargs)):
            self._longargs[i] = '--' + self._longargs[i]
    
    def _argparse(self):
        """_argparse: checks all the arguments and stores error if any
        
        Return:
            actualargs (list): all valid args found.
            argcheck (boolean): Boolean (True: all good, False: Found undefined args)
            argerror (str): error note (if all good, no error note)
            falseargs (list): wrong args if any. (if None, empty list)
        """
        for i in range(len(self._args)):
            if self._args[i] in self._shortargs:
                self._gotargs.append(self._args[i])
            if self._args[i] in self._longargs:
                self._gotargs.append(self._args[i])
        
        for i in range(len(self._args)):
            if self._args[i] not in self._shortargs and self._args[i] not in self._longargs and self._args[i]!='':
                if re.search('--', self._args[i])==None or re.match('-', self._args[i])==None:
                    continue
                self._falseargs.append(self._args[i])
        
        if len(self._falseargs)>0:
            self._argcheck = False
            if len(self._falseargs)==1:
                self._argerror = f'arg {self._falseargs[0]} not found.'
            else:
                self._argerror = 'args '
                for i in range(len(self._falseargs)):
                    self._argerror += f'\'{self._falseargs[i]}\' '
        
                self._argerror += 'not found.'
        
        # if all good then check compulsory args
        if self._argcheck and len(self._compulsory_short)>0 and len(self._compulsory_long):
            for i in range(len(self._compulsory_short)):
                if (self._compulsory_short[i] not in self._gotargs) and (self._compulsory_long[i] not in self._gotargs):
                    self._argerror = f'\'{self._compulsory_short[i]}\' argument is Compulsory'
                    self._argcheck = False
                    break
        
        return self._gotargs, self._argcheck, self._argerror, self._falseargs
    
    def _what_is_(self, arg: str, count=1):
        """
        Returns the value of the argument that is passed.

        Args:
            arg (str): argument you need the value of
            count (int | optional): no of values you are expecting. Default is one

        Returns:
            str | tuple | None_: returns value of argument or None
        """
        if len(arg)>2:
            arg = '--' + arg
        else:
            arg = '-' + arg
        
        try:
            for i in range(len(self._args)):
                if self._args[i] == arg:
                    if count==1:
                        return self._args[i+1]
                    else:
                        k = 1
                        result = []
                        while(count>0):
                            result.append(self._args[i+k])
                            k += 1
                            count -= 1
                        return tuple(result)
        except IndexError:
            raise RuntimeError(f'expects {count} arguments.')
        
        return None