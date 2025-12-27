#!/usr/bin/env python3
"""
Module to serialize and deserialize a custom Python object using pickle
"""

import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the object"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """
        Serialize the current object to a file using pickle

        Args:
            filename (str): The file to save the object to
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            # If saving fails, just return None
            return None

    @classmethod
    def deserialize(cls, filename: str):
        """
        Deserialize a CustomObject instance from a pickle file

        Args:
            filename (str): The file to load the object from

        Returns:
            CustomObject or None: Returns the object if successful, else None
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except (OSError, pickle.PickleError, EOFError):
            return None
