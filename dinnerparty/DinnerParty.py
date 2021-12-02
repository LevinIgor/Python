number = int(input("Enter the number of friends joining (including you):"))

NAMES = []
if number == 0:
    print("No one is joining for the party")
else:  
    for i in range(number):
        NAMES.append(input("Enter the name of every friend (including you), each on a new line:"))
    print(NAMES)
    