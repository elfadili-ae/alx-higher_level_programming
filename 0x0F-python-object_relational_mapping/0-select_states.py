#!/usr/bin/env python3
"""list all states from db"""
from sys import argv
import MySQLdb


db = MySQLdb.connect(host="localhost",
                     user=argv[1],
                     passwd=argv[2],
                     db=argv[3])

cur = db.cursor()

query = "SELECT * FROM states"
cur.execute(query)

for row in cur.fetchall():
    print(row)

cur.close()
db.close()
