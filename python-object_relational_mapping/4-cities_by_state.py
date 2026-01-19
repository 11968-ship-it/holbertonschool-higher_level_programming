#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa along with their states.
Results are sorted by cities.id in ascending order.
"""

import sys
import MySQLdb


def main():
    """
    Connects to a MySQL database and prints all cities with their state names.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
