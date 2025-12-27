#!/usr/bin/env python3
"""
Module to convert CSV data into JSON using serialization
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save it as data.json

    Args:
        csv_filename (str): The path to the CSV file to convert

    Returns:
        bool: True if conversion succeeded, False otherwise
    """
    try:
        # Read CSV data into a list of dictionaries
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data_list = [row for row in reader]

        # Serialize list of dictionaries to JSON and write to file
        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (FileNotFoundError, OSError, csv.Error, json.JSONDecodeError):
        return False
