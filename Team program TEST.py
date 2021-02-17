Teams=[]
while True:
    # command selection from user
    print("Welcome to the Team management program. Please enter a command")
    currentcommand=input("-->")
    # If setup is run
    if currentcommand==("Setup"):
        print("What do you wish the team to be called?")
        currentsetupteam=(input("-->"))

        print("Who do you you wish to add to the team? Type exit when you're done")
        currentpersontoadd=(input("-->"))
        if currentcommand==("exit"):

