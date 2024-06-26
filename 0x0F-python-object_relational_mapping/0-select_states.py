#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == '__main__':
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = connection.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    connection.close()
