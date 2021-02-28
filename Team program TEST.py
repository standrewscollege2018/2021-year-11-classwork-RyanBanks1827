teams = []
teamnames = []
Exit = False
currentpersontoadd="null"

while True:
    # command selection from user
    print("Welcome to the Team management program. Please enter a command")
    currentcommand = input("-->")
    # If setup is run
    if currentcommand == "Setup":
        print("What do you wish the team to be called?")
        currentsetupteam = (input("-->"))
        # This section is the list filling functions which appends certain items to a list.

        while currentpersontoadd != "exit":
            print("Who do you you wish to add to the team? Type exit when you're done")
            currentpersontoadd = input("-->")

            if currentpersontoadd !="exit":
                list.append(teams, [currentpersontoadd])
                list.append(teamnames, [currentsetupteam])

            print(teamnames)
            print(teams)










        print(Teamnames)
        print(Teams)

