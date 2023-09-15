#!/usr/bin/python3
"""List a specific state."""
from sys import argv
from model_state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == argv[4]).all()

    if states == []:
        print("Not found")
    else:
        for state in states:
            print("{}".format(state.id))

    session.close()
