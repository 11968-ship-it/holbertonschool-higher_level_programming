#!/usr/bin/env python3
"""
Module to serialize and deserialize Python dictionaries using XML
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The output XML filename
    """
    # Create root element
    root = ET.Element('data')

    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Store all values as strings

    # Write XML tree to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): The XML file to read from

    Returns:
        dict: Dictionary reconstructed from XML
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}

        for child in root:
            result[child.tag] = child.text  # All values will be strings

        return result

    except (ET.ParseError, FileNotFoundError, OSError):
        return None
