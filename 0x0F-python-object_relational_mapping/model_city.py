#!/usr/bin/python3
"""
This module contains the class definition of a City, which inherits from the Base class from the model_state module. Each instance of the City class represents a row in the 'cities' table in the database.
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    This class defines each city. It inherits from the Base class. Each instance of this class represents a row in the 'cities' table in the database.
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
