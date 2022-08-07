#!/usr/bin/python3
"""ORM Mapping: class definitions of City and instances"""

from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from relationship_state import State


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


State.cities = relationship("City", order_by=City.id,
                            cascade="all, delete,delete-orphan")
