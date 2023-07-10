#!/usr/bin/python3
"""
    This module returns the list of available attributes
    and methods of any object
"""


def lookup(obj):
    """This functions looks out for every attributes and methods of an object"""
    return dir(obj)
