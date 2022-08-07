#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from base import Session, engine, Base


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    """generate database schema"""
    Base.metadata.create_all(engine)
    """create a new session"""
    session = Session()

    st = State(name='California')
    st.cities = [City(name='San Francisco')]
    session.add(st)
    session.commit()
