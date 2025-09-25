def actionInventory():
    if len(inventory) == 0:
        print ("there are no items in your inventory right now")
    else:
        print ("in your inventory you have:", inventory)

def actionStats():
    print (stats)

def question(toAsk, options):
    ask = ""
    while ask not in options:
        ask = input(toAsk)
        if ask not in options:
            print("select a valid answer")
    return (ask)

ask = ""
inventory = []
stats = ["HP 0","ATTACK 0","DEFENCE 0","SPEED 0", "INTELLIGENCE 0", "CHARISMA 0"]
myClass = ""

name = input("Please enter your name adventurer")
myClass = question("Please choose your class: Lawyer, Soldier, Chemist, Trackstar, Bartender", ["Lawyer", "Soldier", "Chemist", "Trackstar", "Bartender"])

if myClass == "Lawyer":
    stats = ["HP 5", "ATTACK 5", "DEFENCE 0", "SPEED 6", "INTELLIGENCE 5", "CHARISMA 10"]
    actionStats()
elif myClass == "Soldier":
    stats = ["HP 8", "ATTACK 10", "DEFENCE 0", "SPEED 5", "INTELLIGENCE 3", "CHARISMA 4"]
    actionStats()
elif myClass == "Chemist":
    stats = ["HP 6", "ATTACK 5", "DEFENCE 0", "SPEED 7", "INTELLIGENCE 10", "CHARISMA 2"]
    actionStats()
elif myClass == "Trackstar":
    stats = ["HP 4", "ATTACK 5", "DEFENCE 0", "SPEED 10", "INTELLIGENCE 4", "CHARISMA 7"]
    actionStats()
else:
    stats = ["HP 10", "ATTACK 6", "DEFENCE 0", "SPEED 3", "INTELLIGENCE 2", "CHARISMA 9"]
    actionStats()

print (ask)
print ("oh, hi there", name, "and welcome to Uravia")
print ("we have been searching for a brave new adventurer such as yourself")
ask = question("Will you help us? y/n", ["y", "n"])
if ask == "y":
    print("Thank you so much")
else:
    print("screw off you're helping anyway")
print("I'm sending you to the centre of our continent where the strife is greatest, please save us all")


