#!/usr/bin/env python3

from os import getcwd as pwd, system
from os.path import join
from re import match

if __name__=='__main__':
    _cd_ = pwd()
    with open(join(_cd_, 'pyproject.toml'), 'r') as t:
        content = t.readlines()
    
    for c in content:
        c = c.replace('\n', '')
        if match(r'^version', c):
            version = c.split(' ')[len(c.split(' '))-1].replace('\"', '')
    
    system(f'pip install optioner=={version}')