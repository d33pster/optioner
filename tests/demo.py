#!/usr/bin/env python3


from sys import argv
from optioner import options

shortargs = ['o1', 'o2', 'o3']
longargs = ['option1', 'option2', 'option3']
ignore = ['--option2', '-o2']
compulsory_s = ['o3']
compulsory_l = ['option3']
ifthisthennotthat = [['o1','option1'],['o3', 'option3']]

ctrl = options(shortargs, longargs, argv[1:], compulsory_s, compulsory_l, ignore, ifthisthennotthat)
args, check, error, falseargs = ctrl._argparse()

try:
    arr = args[0]
    if len(args)>1:
        for i in range(1, len(args)):
            arr += f":{args[i]}"
    else:
        pass
except IndexError:
    arr = ''

print(arr)
print(check)
print(error)
print(ctrl._what_is_(args[0].split('-')[len(args[0].split('-'))-1]))