# importing the sqlite library
import sqlite3

# defining our database that we're gonna access, if not already existant, it should just be created.
DATABASE = 'Test database.db'

# connect
connection=sqlite3.connect(DATABASE)


