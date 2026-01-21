#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
using SQLAlchemy ORM.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")

    session.close()
