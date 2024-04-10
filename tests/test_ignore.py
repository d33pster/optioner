#!/usr/bin/env python3

from os import popen, getcwd
from os.path import join

def test_one():
    """test case 6:
    test ignore
    """
    
    output = popen(f"python3 {join(getcwd(), 'tests', 'demo.py')} -o2 hehe").readlines()
    
    assert output[1].replace('\n','') == 'True'