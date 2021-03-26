#!/usr/bin/python3


""" Module 4-cities_by_state"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8",
    )
    cur = db.cursor()
    statement = """SELECT cities.id, cities.name, states.name
                 FROM cities, states
                 WHERE cities.state_id = states.id
                 ORDER BY cities.id ASC"""
    cur.execute(statement)
    all_rows = cur.fetchall()
    for row in all_rows:
        print(row)
    cur.close()
    db.close()
