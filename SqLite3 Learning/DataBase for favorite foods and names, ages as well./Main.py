# importing the sqlite library
import sqlite3

# defining our database that we're gonna access, if not already existant, it should just be created.
DATABASE = 'FreindDB.db'

# connect
connection=sqlite3.connect(DATABASE)

cursor=connection.cursor()
# Full SQLITE capability enabled
connection.execute("PRAGMA foreign_keys = ON")

# Create the student tables if they do not already exist




cursor.execute("""CREATE TABLE IF NOT EXISTS Freind(
freindid INTEGER PRIMARY KEY, 
freindname TEXT UNIQUE NOT NULL,
freindfavfood TEXT UNIQUE NOT NULL,
freindage INTEGER NOT NULL,
tutor_id INTEGER NOT NULL,

)""")

# inserting records into the student table and tutor table.
# cursor.execute("INSERT INTO tutor(tutor_code) VALUES('ABC'), ('xyz')")
cursor.execute("INSERT INTO student(student_name, student_age, tutor_id) VALUES ('Toby', 16, 2), ('Isaac', 15, 2), ('sam', 14, 2)")
print("Welcome to the freind Database.")
enteredname=input("Please enter your name :")

cursor.execute("INSERT INTO Freind(freindname, VALUES (enteredname))")

# selects all student names.
# makes names type array
connection.commit()
names=cursor.execute("SELECT student_name, student_age FROM student")
# loops through array, therefor printing all data
for name in names:
    print(name[0], name[1])
