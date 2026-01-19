#!/usr/bin/python3
"""
This module defines a State class mapped to the 'states' table
in a MySQL database
using SQLAlchemy ORM. It also provides the Base instance for
table creation.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Base class for declarative class definitions
Base = declarative_base()


class State(Base):
    """
    State class mapped to the 'states' table.

    Attributes:
        id (int): Auto-incremented primary key, cannot be null.
        name (str): Name of the state, max 128 characters, cannot be null.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
