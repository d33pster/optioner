# optioner

![Static Badge](https://img.shields.io/badge/pypi-available-brightgreen?style=flat&logo=python&logoColor=red)
![Static Badge](https://img.shields.io/badge/Linux-supported-blue?style=flat&logo=Linux&logoColor=red)
![Static Badge](https://img.shields.io/badge/Windows-supported-blue?style=flat&logo=Windows&logoColor=red)
![Static Badge](https://img.shields.io/badge/MacOS-supported-blue?style=flat&logo=Macintosh&logoColor=red)
![Static Badge](https://img.shields.io/badge/python-only-green?style=flat&logo=python&logoColor=red)
<br><br><br>
v1.0

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
# create argument control
>>> arg_control = options(shortargs, longargs, sys.argv[1:])
# get values
>>> actualargs, argcheck, argerror, falseargs = arg_control._argparse()
```

## Extra features
Added a function to query argument value.
