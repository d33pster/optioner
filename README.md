# optioner

![Static Badge](https://img.shields.io/badge/pypi-available-brightgreen?style=flat&logo=python&logoColor=red)
![Static Badge](https://img.shields.io/badge/Linux-supported-blue?style=flat&logo=Linux&logoColor=red)
![Static Badge](https://img.shields.io/badge/Windows-supported-blue?style=flat&logo=Windows&logoColor=red)
![Static Badge](https://img.shields.io/badge/MacOS-supported-blue?style=flat&logo=Macintosh&logoColor=red)
![Static Badge](https://img.shields.io/badge/python-only-green?style=flat&logo=python&logoColor=red)
<br><br><br>
v1.3.5

<p align='center'>
    <a href='#Installation'>Installation</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='#Usage'>Usage</a>
</p><br>

## About
Optioner is a lightweight Argument Parser and easy to use.

## Installation
```console
$ pip install optioner
```

## Usage

###### initialization
```console
>>> from optioner import options
>>> help(options)

Help on class options in module optioner:

class options(builtins.object)
 |  options(shortargs: list, longargs: list, gotargs: list)
 |
 |  Methods defined here:
 |
 |  __init__(self, shortargs: list, longargs: list, gotargs: list)
 |      init function: This runs everytime the class is called.
 |
 |      Args:
 |          shortargs (list): example: ['h', 'l', 'i', ...]
 |          longargs (list): example: ['help', 'lock', 'init', ...]
 |          gotargs (list): sys.argv[1:]
 |          compulsort (list | optional): optional compulsory arguments
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
```
###### use method

after creating class object, call _argparse() method

help:
```console
>>> help(options._argparse)

Help on function _argparse in module optioner:

_argparse(self)
    _argparse: checks all the arguments and stores error if any

    Return:
        actualargs (list): all valid args found.
        argcheck (boolean): Boolean (True: all good, False: Found undefined args)
        argerror (str): error note (if all good, no error note)
        falseargs (list): wrong args if any. (if None, empty list)
```

usage:
```console
# import module
>>> from optioner import options
>>> import sys
# define short args
>>> shortargs = ['a', 'b']
# define long args
>>> longargs = ['assign', 'bind']
# create option control
>>> optionCTRL = options(shortargs, longargs, sys.argv[1:])
# get values
>>> actualargs, argcheck, argerror, falseargs = optionCTRL._argparse()
```

## Extra features
Added a function to query argument value.
```console
>>> help(options._what_is)

Help on function _what_is_ in module optioner:

_what_is_(self, arg: str)
    Returns the value of the argument that is passed.

    Args:
        arg (str): argument you need the value of
        count (int | optional): no of values you are expecting. Default is one

    Returns:
        str | tuple | None_: returns value of argument or None
```

usage:
```console
>>> optionCTRL = options(shortargs, longargs, gotargs)
>> optionCTRL._argparse()

>>> optionCTRL._what_is_(shortargs[0])

or 

>>> optionCTRL._what_is_(longargs[0])
```