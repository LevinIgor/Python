import random
import sys

NUMBER = int(input("Enter the number of friends joining (including you): "))

NAMES = {}

if NUMBER == 0: 
    print("No one is joining for the party") 
    sys.exit()
    
 
for i in range(NUMBER):
    NAMES[input("Enter the name of every friend (including you), each on a new line: ")] = 0

TOTAL = int(input("Enter the total amount: "))
ANSWER = input("Do you want to use the 'Who is lucky?' feature? Write y/n: ")

if ANSWER == 'y':
    lucky = str(random.choice(list(NAMES)))
    print(lucky + " is the lucky one!" )
    for i in NAMES:
        NAMES[i] = TOTAL / (NUMBER-1) if i != lucky else 0
    print(NAMES)
    sys.exit()


print("No one is going to be lucky")
for i in NAMES:
    NAMES[i] = round(TOTAL/NUMBER,2) 
print(NAMES)


    