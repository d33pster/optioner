#!/usr/bin/env python3

from os import popen, getcwd
from os.path import join

def test_one():
    """test case 7:
    test ifthisthennotthat
    """
    
    output = popen(f"python3 {join(getcwd(), 'tests', 'demo.py')} -o1 hehe -o3 huhu").readlines()
    
    assert output[1].replace('\n','') == 'False'