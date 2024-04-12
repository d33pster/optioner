#!/usr/bin/env python3

from sys import argv
from optioner import options

shortargs = ['o1', 'o2', 'o3']
longargs = ['option1', 'option2', 'option3']
ignore = ['--option2', '-o2']
compulsory_s = ['o3']
compulsory_l = ['option3']
ifthisthennotthat = [
    ['o1','option1'],['o3', 'option3'],
    ['hehe', 'huhu'], ['o3', 'option3']
]

ctrl = options(shortargs, longargs, argv[1:], compulsory_s, compulsory_l, ignore, ifthisthennotthat)
args, check, error, falseargs = ctrl._argparse()

print(check)
print(error)