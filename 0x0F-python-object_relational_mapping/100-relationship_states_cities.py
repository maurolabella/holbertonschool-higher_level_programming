#!/usr/bin/python3
"""Start link class to table in database
"""
from relationship_state import State
from relationship_city import City
from base import Session, engine, Base


if __name__ == "__main__":
    """generate database schema"""
    Base.metadata.create_all(engine)
    """create a new session"""
    session = Session()

    st = State(name='California')
    st.cities = [City(name='San Francisco')]
    session.add(st)
    session.commit()
