# Importing SQlite
import sqlite3
import time
DELAY=0.1
Checklist = 'Checklist.db'
# Connecting to the Database
connection = sqlite3.connect(Checklist)
time.sleep(DELAY)
# Adds The cursor, the cursor is used to modify tables and such, so it's important to identify it
# in a variable so we may use it in later use!
cursor = connection.cursor()
# Unlocking full capability of sqlite, so we can use NOT NULL values.
connection.execute("PRAGMA foreign_keys = ON")
time.sleep(DELAY)
cursor.execute("""CREATE TABLE IF NOT EXISTS To-do(
Showing value INTEGER PRIMARY KEY, Complete BOOLEAN UNIQUE NOT NULL)""")

time.sleep(DELAY)
connection.commit()

time.sleep(DELAY)
while(True):
    COMMAND=input("Enter a command!")
    time.sleep(DELAY)