#!/usr/bin/python3


""" Module 13-model_state_delete_a"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_usr = argv[1]
    mysql_pswd = argv[2]
    db_name = argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            mysql_usr, mysql_pswd, db_name
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result_states = session.query(State).order_by(State.id).all()
    for state in result_states:
        if "a" in state.name:
            session.delete(state)
    session.commit()
