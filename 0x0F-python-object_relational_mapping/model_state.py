#!/usr/bin/python3
"""ORM Mapping: class definitions of State and instances"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ORM MAPPING: class State <-->state table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement="auto", unique=True)
    name = Column(String(128), nullable=False)
