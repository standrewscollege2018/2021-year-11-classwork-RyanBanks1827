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

# inserting records into the student table and tutor table.
# cursor.execute("INSERT INTO tutor(tutor_code) VALUES('ABC'), ('xyz')")
#cursor.execute("INSERT INTO student(student_name, student_age, tutor_id) VALUES ('Toby', 16, 2), ('Isaac', 15, 2), ('sam', 14, 2)")


# selects all student names.
# makes names type array
connection.commit()
names=cursor.execute("SELECT student_name, student_age FROM student")
# loops through array, therefor printing all data
for name in names:
    print(name[0], name[1])



