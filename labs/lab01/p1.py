# Filename: p1.py
# Author: MIDN 2/C Ian Coffey (m261194)
# To read in file data to manage groceries

# Read & Open File 
fName = str(input("Filename: "))
try:
    file = open(fName, "r")
except OSError as e:
    print("File not found!")
    exit(1)

# Save Fruit Prices in Dict
fruitDict = {}
with open(fName, "r") as f:
    for line in f:
        parse = line.split()
        fruitDict[parse[0]] = parse[1]

# Variable Declarations
total = 0.0
cmd = ""

# While Loop to Read Commands
while (cmd != "checkout"):
    cmd = str(input("command: "))
    parse = cmd.split()

    # If User is adding an item
    if (parse[0] == "add"):
        numItem = float(parse[1])
        item = parse[3]

        # Check if item exists in Dict
        if item in fruitDict.keys():
            # Update Total
            total = total + (numItem * float(fruitDict.get(item)))
        else:
            print("Error! " + item + " not found!")

    # If User wants to check the price of an item
    elif (parse[0] == "price"):
        # Grab item from Dict
        item = parse[1]
        if item in fruitDict.keys():
            print(item + " are " + fruitDict.get(item) + " per pound")
        else:
            print("Error! " + item + " not found!")

# Calculate Total
print("total is " + f"{total:.2f}")
exit(0)
 
        
    

