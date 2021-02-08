# importing the sqlite library
import sqlite3

# defining our database that we're gonna access, if not already existant, it should just be created.
DATABASE = 'Test database.db'

# connect
connection=sqlite3.connect(DATABASE)

cursor=connection.cursor()
# Full SQLITE capability enabled
connection.execute("PRAGMA foreign_keys = ON")

# Create the student tables if they do not already exist

cursor.execute("""CREATE TABLE IF NOT EXISTS tutor(
tutor_id INTEGER PRIMARY KEY, tutor_code TEXT UNIQUE NOT NULL)""")


cursor.execute("""CREATE TABLE IF NOT EXISTS student(
student_id INTEGER PRIMARY KEY, 
student_name TEXT UNIQUE NOT NULL,
student_age INTEGER NOT NULL,
tutor_id INTEGER NOT NULL,
FOREIGN KEY(tutor_id) REFERENCES tutor(tutor_id) ON DELETE CASCADE
)""")


