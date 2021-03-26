#!/usr/bin/python3


""" Module 10-model_state_my_get"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_usr = argv[1]
    mysql_pswd = argv[2]
    db_name = argv[3]
    st_name = argv[4]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            mysql_usr, mysql_pswd, db_name
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result_state = session.query(State).filter(State.name == st_name).first()
    print(result_state.id if result_state else "Not found")
