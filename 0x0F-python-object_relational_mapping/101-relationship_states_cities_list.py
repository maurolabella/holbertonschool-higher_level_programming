#!/usr/bin/python3
"""scrip that lists all State objects, and corresponding
City contained in the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    """generate database schema"""
    Base.metadata.create_all(engine)
    session = Session()

    result = session.query(State).join(City)
    for row in result:
        print(f"{row.id}:  {row.name}")
        for city in row.cities:
            print(f"    {city.id}: {city.name}")
