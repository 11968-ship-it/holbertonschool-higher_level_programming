#!/usr/bin/python3
"""
Lists all states with a name starting with N (uppercase only)
from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Execute query with filter for uppercase N
    cursor.execute(
        "SELECT * FROM states "
        "WHERE BINARY name LIKE 'N%' "
        "ORDER BY id ASC"
    )

    # Fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close connection
    cursor.close()
    db.close()
