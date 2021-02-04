
while(True):

    personwhojustusedit=input("Hi random person, leave your name here and the script will save it!")
    if(personwhojustusedit=="debug"):
        f=open("users.txt", "r")
        print(f.read())
    else:
        f = open("users.txt", "a")
        f.write(personwhojustusedit)
        f.close()





