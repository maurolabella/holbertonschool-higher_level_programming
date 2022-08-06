#!/usr/bin/python3
"""SQLAlchemy ORM: Creating Session and Query on states
   query(State), sql_injection aware
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
    st_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)
    res = states.filter_by(name=st_name).first()
    print(res.id if res else "Not found")

    session.close()


if __name__ == '__main__':
    main()
