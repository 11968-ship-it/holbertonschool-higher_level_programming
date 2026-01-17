#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa where name matches
the argument (case-sensitive).
"""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Case-sensitive SQL query
    query = ("SELECT * FROM states WHERE BINARY name = '{}' "
             "ORDER BY id ASC").format(state_name)
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
