#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    nmeSr = "SELECT * FROM states WHERE name LIKE BINARY '{}'"\
            .format(sys.argv[4])
    cur.execute(nmeSr)
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
