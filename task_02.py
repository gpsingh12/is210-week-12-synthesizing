#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02"""


class CustomError(Exception):
    """ Exception is parent class for CustomError.
    Attributes:
        None
    """

    def __init__(self, param, cause):
        """Constructor for CustomError class.
        Args:
            cause(str): stores value
            param(str): default partameter
        Attributes:
            cause(str):
        """
        self.cause = cause
        self.param = param
        Exception.__init__(self)
