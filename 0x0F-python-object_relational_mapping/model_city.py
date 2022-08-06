#!/usr/bin/python3
"""ORM Mapping: class definitions of City and instances"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """ORM MAPPING: class City <-->cities table"""
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement="auto",
                unique=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
