#!/usr/bin/python3
""" list all cities """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id)
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
