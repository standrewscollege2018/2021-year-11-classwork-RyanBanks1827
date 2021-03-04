import sqlite3
# Connecting and creating the database if not already existant
DATABASE = "Student Database.db"
connection = sqlite3.connect(DATABASE)
#Making the cursor
cursor = connection.cursor()
connection.execute("PRAGMA foreign_keys= ON")
#Functions go here:
# cursor.execute("""CREATE TABLE STUDENT(name text, Gender Text) """)
Nametoadd=str(input("What is the name of the student you wish to add to the database?"))
print("Going to add "+Nametoadd)
genderselect=input("What gender are they?")
if genderselect=="male":
    gendertoadd="M"
elif genderselect=="female":
    gendertoadd="F"
students= cursor.execute("SELECT STUDENT")

cursor.execute("INSERT INTO STUDENT VALUES('Max', 'M')")
connection.commit()
connection.close()