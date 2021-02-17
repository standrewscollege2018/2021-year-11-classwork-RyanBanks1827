Teams = []
Teamnames = []
Exit=False
while True:
    # command selection from user
    print("Welcome to the Team management program. Please enter a command")
    currentcommand = input("-->")
    # If setup is run
    if currentcommand == "Setup":
        print("What do you wish the team to be called?")
        currentsetupteam = (input("-->"))
# This section is the list filling functions which appends certain items to a list.
        while not Exit:
            print("Who do you you wish to add to the team? Type exit when you're done")
            currentpersontoadd = (input("-->"))
            list.append(Teams, [currentpersontoadd])
            list.append(Teamnames, [currentsetupteam])
            print(Teamnames)
            print(Teams)
            if currentpersontoadd=="exit":
                Exit=True

        print(Teamnames)
        print(Teams)
        print("NiceS")
