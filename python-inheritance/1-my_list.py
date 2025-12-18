#!/usr/bin/python3
"""
Module that definesoka MyList, a list subclass with a print_sorted method
"""

class MyList(list):
    """
    This class prints a sorted list
    """
  
    def print_sorted(self):
        """
        Prints a sorted copy of the list without modifying the original list
        """
        print(sorted(self))
