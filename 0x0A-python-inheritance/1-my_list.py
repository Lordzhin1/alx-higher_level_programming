#!/usr/bin/python3
"""This module acquires from the list class"""


class MyList(list):
    """A class that acquires from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
