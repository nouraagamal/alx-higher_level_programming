#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing
the letter a from the database
Using module SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    state_del = session.query(State).filter(State.name.like('%a%')).all()
    for i in state_del:
        session.delete(i)
    session.commit()
    session.close()
