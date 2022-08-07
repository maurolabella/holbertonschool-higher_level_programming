#!/usr/bin/python3
"""ORM Mapping: class definitions of State and instances"""

from requests import delete
from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base


class State(Base):
    """ORM MAPPING: class State <-->state table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement="auto", unique=True)
    name = Column(String(128), nullable=False)
