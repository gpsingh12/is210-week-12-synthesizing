#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""


class BaseError(Exception):
    """Exception is parent class for BaseError.
    Attributes:
        None
    """
    pass


class StringError(BaseError, TypeError):
    """BaseError and TypeError are parent classes for StringError.
    Attributes:
        None
    """
    pass


class NumberError(BaseError, TypeError):
    """BaseError and TypeError are parent classes for StringError.
    Attributes:
        None
    """
    pass


class NonZeroError(NumberError):
    """NumberError is parent class for NonZeroError.
    Attributes:
        None
    """
    pass
