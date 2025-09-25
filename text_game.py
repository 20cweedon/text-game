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

name = input("Please enter your name adventurer")
print ("please choose your class")
ask 
print ("oh, hi there", name, "and welcome to Uravia")
print ("we have been searching for a brave new adventurer such as yourself")
ask = input("Will you help us? y/n")
if ask == y:
    print("thank you so much you kind soul")
else:
    print("fuck off you're helping anyway")
print("I'm sending you to the centre of our continent where the strife is greatest, please save us all")

ask = input("Grab, Use, Talk, Run, Attack")
if ask == "Grab":
    actionInventory()