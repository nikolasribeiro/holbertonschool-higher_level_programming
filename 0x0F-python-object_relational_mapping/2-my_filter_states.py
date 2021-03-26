#!/usr/bin/python3


""" Module 2-my_filter_states"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    name_to_search = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8",
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY id ASC".format(
            name_to_search
        )
    )
    all_rows = cur.fetchall()
    for row in all_rows:
        print(row)
    cur.close()
    db.close()
