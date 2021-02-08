# importing the sqlite library
import sqlite3

# defining our database that we're gonna access, if not already existant, it should just be created.
DATABASE = 'Test database.db'

# connect
connection=sqlite3.connect(DATABASE)


# inserting records into the student table and tutor table.
# cursor.execute("INSERT INTO tutor(tutor_code) VALUES('ABC'), ('xyz')")
cursor.execute("INSERT INTO student(student_name, student_age, tutor_id) VALUES ('Toby', 16, 1), """)
   #TBC
               "