#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
using SQLAlchemy ORM.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print(
            "Usage: ./7-model_state_fetch_all.py <username> "
            "<password> <database>"
        )
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all State objects, ordered by id ascending
    states = session.query(State).order_by(State.id).all()

    # Print each state
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
