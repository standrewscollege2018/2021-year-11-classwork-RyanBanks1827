# Imports
import random
import time

timer = 6
winningthing = "A new car"
# Setting the delay variable for how fast the program will run/
DELAY = 0.1
# Defining the raffle list to be accessed and appended to later
raffle = []


# defining the test function- this function makes sure the string doesn't contain integers
def test(obj):
    try:
        int(obj) or float(obj)

        return True
    except ValueError:
        return False


# Main loop for command setting.
while True:
    raffleinput = input("enter your name to be in to win: " + winningthing + " ")
    # Determining the raffle length so the name can be drawn
    if raffleinput == "devrun":
        rafflelength = len(raffle)
        result = random.randint(0, rafflelength)
        # defining name using this list position now picked.
        winner = raffle[result]
        print("Drumroll please!")
        time.sleep(DELAY)
        while timer > 1:
            print("tst")
            timer = timer - 0.1
            time.sleep(0.1)
        print(winner)
        print("Has won: " + winningthing)
    # Allows devs to change the prize.
    if raffleinput == "changeprize":
        winningthing = input("New prize?--> ")
        print(winningthing + " Is the new prize.")
    # Triggers if the raffleinput test fails -ln 12 for reference.
    if test(raffleinput):
        print("That's not a name! You slimy sea slug!")
    if raffleinput == "listclear":
        raffle = []
    # Appending to the list the proper value while letting the user know what they entered.
    elif raffleinput != "changeprize" or raffleinput != "devrun" or raffleinput != "listclear":
        list.append(raffle, raffleinput)
        print("Added " + raffleinput + " to the list! ")
        time.sleep(DELAY)
