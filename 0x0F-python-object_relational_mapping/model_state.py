#!/usr/bin/python3
"""
This module contains the class definition of a State, which inherits from the Base class. Each instance of the State class represents a row in the 'states' table in the database.
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """
    This class defines each state. It inherits from the Base class. Each instance of this class represents a row in the 'states' table in the database.
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
