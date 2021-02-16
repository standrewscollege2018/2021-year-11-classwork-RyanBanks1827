import time
versionnumber = 0.2
BTD = 0.3
# Registers the List variable of the program.
Teamnames = []
TeamPeople = []
teammembers=[]

def command_add(teamtoregister):
    print("Registered the team :" + str(teamtoregister))
    registerteam = str(teamtoregister)
    list.append(Teamnames, registerteam)


def command_remove(teamtoremove):
    print("deleting team "+teamtoremove)
    teamtoremove.clear()


def command_register(person):
    AddID = input("Which team do you wish to assign this person to?")
    if AddID in Teamnames:
        # AddID is used to describe what team you wish to add the person to
        # Person is just the imported variable used in the function
        # Remember that, Toby!

        print("Assigned person to the team: " + AddID)
        time.sleep(BTD)
        teampeople = [person, AddID]
        teammembers = [[Teamnames], [teampeople]]


    else:
        print("Oops, It appears that the """ + AddID +
              """team doesn't exist! Please use the add command to make this team before assigning people!""")
    time.sleep(BTD)
def command_list_members(Teamname):
    print("The list of people in the " +Teamname+" Team is as follows")
    time.sleep(BTD)
    print(teammembers)

Currentcommand = "NULL"

# Main loop
while (True):
    print("Welcome to the team manager!" + "Version " + str(versionnumber))
    time.sleep(BTD)
    print("Enter a command!")
    time.sleep(BTD)
    Currentcommand = input("->")

    if Currentcommand == "help" or Currentcommand == "Help":
        print("Use the command Add to create a new team")
        time.sleep(BTD)
        print("Use the command Remove to delete a stored team.")
        time.sleep(BTD)
        print("Use the command Register to begin registering a person to a currently existing team")
        time.sleep(BTD)
        print("Use the command List to list all current teams registered.")
        time.sleep(BTD)

        print("Use the memberlist command to see which people are in which team! ")
        print("""SIDE NOTE: All commands can be entered with a capital 
                                   first letter or lower case first letter
                                    which is there purely for convenience.""")
        time.sleep(BTD)


    elif Currentcommand == "Add" or Currentcommand == "add":
        # Importing user decision into a function is fun!
        print("What do you wish this team to be called?")
        teamadd = input("-->")
        command_add(teamadd)


    elif Currentcommand == "Remove" or Currentcommand == "remove":
        # Simple remove command --coming soon--

        print("Which team do you wish to remove?")

    elif Currentcommand == "List" or Currentcommand == "list":
        print("The current teams are :")
        time.sleep(BTD)

        if len(Teamnames) == 0:
            print("Oops, looks like you havn't  any teams yet!, Make sure you do that before attempting to list!")
            time.sleep(BTD)

        else:
            print(Teamnames)
            time.sleep(BTD)
            time.sleep(BTD)
            print("""Use List or list followed by the name of the team, 
                          in order to read the list of team members!""")

            time.sleep(BTD)

    elif Currentcommand == "Register" or Currentcommand == "register":
        entity = input("What is the name of the person to register?")
        time.sleep(BTD)
        command_register(person=entity)

    elif Currentcommand == "Memberlist" or Currentcommand =="memberlist":
        whichteamtolist =input("Which team do you wish to retrieve all members from?")
        command_list_members(whichteamtolist)









    else:
        print("use the command help to look at a list of commands ")
    time.sleep(BTD)
    time.sleep(BTD)
    time.sleep(BTD)
