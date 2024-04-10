#!/usr/bin/env python3

from os import popen, getcwd
from os.path import join

def test_one():
    """test case 1:
    test options class methods against a predefined conditions
    """
    output = popen(f"python3 {join(getcwd(), 'tests', 'demo.py')} -o2").readlines()
    
    assert output[0].replace('\n','') == '-o2'
    assert output[1].replace('\n','') == 'True'

def test_two():
    """test case 2:
    test options class for wrong arg
    """
    output = popen(f"python3 {join(getcwd(), 'tests', 'demo.py')} -o hehe").readlines()
    
    assert output[1].replace('\n','') == 'False'

def test_three():
    """test case 3:
    test options class for value
    """
    output = popen(f"python3 {join(getcwd(), 'tests', 'demo.py')} -o3 hehe").readlines()
    
    assert output[0].replace('\n','') == '-o3'
    assert output[1].replace('\n','') == 'True'
    assert output[3].replace('\n','') == 'hehe'

def test_four():
    """test case 4:
    test options class for multiple values
    """
    
    output = popen(f"python3 {join(getcwd(), 'tests', 'demo2.py')} -o3 hehe huhu").readlines()
    
    assert output[0].replace('\n','') == 'hehe'
    assert output[1].replace('\n','') == 'huhu'