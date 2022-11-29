import sqlite3
from sqlite3 import Error
import os
import sys
import json

database = os.path.join(os.getcwd(), "database_new", "film_dataa.db")
print(database)
try:
    conn = sqlite3.connect(database)
except Error as e:
    print(e)
    sys.exit()

curs = conn.cursor()

##ex1
# curs.execute("SELECT title FROM film_data WHERE title like 'B%' ")
# print(curs.fetchall())
# conn.commit()

##Ex2
# curs.execute("SELECT MAX(length) FROM film_data")
# print(curs.fetchall())
# conn.commit()

##ex3
# curs.execute("SELECT * FROM film_data")

# b = curs.fetchall()
#
# with open("db.json", "w") as f:
#     c = f.write(str(b))

curs.execute("SELECT title FROM film_data WHERE release_year > 2010 AND rate BETWEEN 3 AND 5 ")
print(curs.fetchall())
conn.commit()


# filtered_film
conn.close()
