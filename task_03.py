#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""

def exception_test(arg1, arg2, arg3):
    """Function uses try and except blocks to return error.
    Arg:
        arg1(list): input arg 1
        arg2(int): input arg 2
        arg3(str): input arg 3
    Return:
        returns boolean True or False or errors if the conditions
        are not met.
    Examples:
        >>>exception_test(['apple'], 0, 'p')
        False
        >>> exception_test(43, 1, 1)
        True
        >>>exception_test(['apple'], 0, x)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        NameError: name 'x' is not defined
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (TypeError, KeyError, IndexError):
        caught = True

    return caught
    
