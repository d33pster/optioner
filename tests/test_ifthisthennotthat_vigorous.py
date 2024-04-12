#!/usr/bin/env python3

from os import popen, getcwd
from os.path import join

def test():
    output = popen(f"python3 {join(getcwd(), 'tests', 'demo3.py')} hehe").readlines()
    
    assert output[1].replace('\n','') == 'undefined argument \'huhu\''
    assert output[0].replace('\n','') == 'False'