#!/usr/bin/python3
"""
Lists all states with a name starting with N (case-insensitive) from the database hbtn_0e_0_usa
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

    # Execute query with case-insensitive filter
    cursor.execute(
        "SELECT * FROM states WHERE name COLLATE utf8mb4_general_ci LIKE 'N%' ORDER BY id ASC"
    )

    # Fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close connection
    cursor.close()
    db.close()
