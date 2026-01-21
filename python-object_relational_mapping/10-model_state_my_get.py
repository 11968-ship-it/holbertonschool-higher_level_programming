#!/usr/bin/python3
"""
Prints the id of the State object with the name passed as argument
from the database hbtn_0e_6_usa using SQLAlchemy ORM.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
        State.name == state_name
    ).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
