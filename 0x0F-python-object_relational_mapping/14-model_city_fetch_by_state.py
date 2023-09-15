#!/usr/bin/python3
"""List cities."""
from sys import argv
from model_state import State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State) \
                              .filter(State.id == City.state_id)\
                              .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
