#!/usr/bin/env python3

import re

class options:
    def __init__(self, shortargs: list, longargs: list, gotargs: list):
        """init function: This runs everytime the class is called.

        Args:
            shortargs (list): example: ['h', 'l', 'i', ...]
            longargs (list): example: ['help', 'lock', 'init', ...]
            gotargs (list): sys.argv[1:]
        """
        self._args = gotargs
        self._shortargs = shortargs
        self._longargs = longargs
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
        
        return self._gotargs, self._argcheck, self._argerror, self._falseargs
    
    def _what_is_(self, arg: str):
        """
        Returns the value of the argument that is passed.

        Args:
            arg (str): argument you need the value of

        Returns:
            str | None_: returns value of argument or None
        """
        if len(arg)>2:
            arg = '--' + arg
        else:
            arg = '-' + arg
        
        for i in range(len(self._args)):
            if self._args[i] == arg:
                return self._args[i+1]
        
        return None