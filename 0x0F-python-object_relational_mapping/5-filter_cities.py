#!/usr/bin/python3


""" Module 5-filter_cities"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_to_search = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8",
    )
    cur = db.cursor()
    statement = """SELECT cities.name
                 FROM cities, states
                 WHERE BINARY states.name = %s
                 AND cities.state_id = states.id
                 ORDER BY cities.id ASC"""
    cur.execute(statement, (state_to_search,))
    all_rows = cur.fetchall()
    print(", ".join(row[0] for row in all_rows))
    cur.close()
    db.close()
