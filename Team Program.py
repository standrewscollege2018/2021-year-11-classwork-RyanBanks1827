# Registers the List variable of the program.
Teamnames = []


def command_add(teamtoregister):
    print("Registered the team :" + str(teamtoregister))
    registerteam = str(teamtoregister)
    list.append(Teamnames, registerteam)


def command_remove(Teamtoremove):
    print("Haha not implemented yet!")


# Importing modules
import time

BTD = 0.1
Currentcommand = ("NULL")
versionnumber = 0.1
# Main loop
while (True):
    print("Welcome to the team manager!" + "Version " + str(versionnumber))
    time.sleep(BTD)
    print("Enter a command!")
    time.sleep(BTD)
    Currentcommand = input("->")

    if Currentcommand == "help" or Currentcommand == "Help":
        print("Use the command Add-Capital or Non capital to create a new team")
        time.sleep(BTD)
        print("Use the command Remove to delete a stored team- Capital or non capital")
        time.sleep(BTD)
        print("Use the command Register to begin registering a person to a currently existing team")
        time.sleep(BTD)


    elif Currentcommand == "Add" or Currentcommand == "add":
        # Importing user decision into a function is fun!
        print("What do you wish this team to be called?")
        teamadd = input("-->")
        command_add(teamadd)

    elif Currentcommand == "Remove" or Currentcommand == "remove":
        # Simple remove command --coming soon--

        print("Which team do you wish to remove?")

    elif Currentcommand == "Read" or Currentcommand == "read":
        print("The current teams are :")
        time.sleep(BTD)
        print(Teamnames)
        if Teamnames== "[]":
            print("Oops, looks like you havn't added a team yet!, Make sure you do that before attempting to list!")

        else:
            print("""Use Read or read followed by the name of the team, 
                          in order to read the list of team members!""")
            time.sleep(BTD)









    else:
        print("use the command help to look at a list of commands ")
