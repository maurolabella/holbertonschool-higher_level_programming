#!/usr/bin/python3
"""SQLAlchemy ORM: Creating Session and Query on states
   session.add(object)
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """ main function"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        x = session.query(State).get(2)
        x.name = "New Mexico"
    except Exception:
        pass

    session.commit()

    session.close()


if __name__ == '__main__':
    main()
