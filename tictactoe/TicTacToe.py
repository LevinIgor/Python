

def printfield():
    print(f"""
    {field[0][0]} {field[0][1]} {field[0][2]}
    {field[1][0]} {field[1][1]} {field[1][2]}
    {field[2][0]} {field[2][1]} {field[2][2]}
    """)

def isWin():
    oList = ["O","O","O"]
    xList = ["X","X","X"]
    
    if (field[0] == oList or field[0] == xList)or(field[1] == oList or field[1] == xList)or(field[2] == oList or field[2] == xList):
        return True
    if (field[0][0]==field[1][0]==field[2][0] == "X" or field[0][0]==field[1][0]==field[2][0] == "O") or (field[0][1]==field[1][1]==field[2][1] == "X" or field[0][1]==field[1][1]==field[2][1] == "O") or (field[0][2]==field[1][2]==field[2][2] == "X" or field[0][2]==field[1][2]==field[2][2] == "Y"):
        return True
    if (field[0][0] and field[1][1] and field[2][2] == "X" or field[0][0] and field[1][1] and field[2][2] == "O") or (field[0][2] and field[1][1] and field[2][0] == "X" or field[0][2] and field[1][1] and field[2][0] == "O"):
        return True
    
    return False

def clearField():
    global field
    field = [['-','-','-'],['-','-','-'],['-','-','-']]

field = []
clearField()
printfield()
current = "X"
while True:
    print("Enter the coordinates:")
    coord = input()
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    if len(coord) == 3 and coord[1] ==" ":
        if coord[0] in numbers and coord[2] in numbers: 
            xCord = int(coord[0])-1
            yCord = int(coord[2])-1
        else:
            print("You should enter numbers!")
            continue
    else:
        print("Enter coordinate types (X Y)")
        continue
    if (xCord or yCord) > 2 or (xCord or yCord) < 0:
        print('Coordinates should be from 1 to 3!') 
    else:
        if field[xCord][yCord] == "-":
            field[xCord][yCord] = current
            if current == "X": current = "O" 
            else: current = "X"
        else:
            print("This cell is occupied! Choose another one!")
    printfield()

    if field[0].count('-') == 0 and field[1].count('-') == 0 and field[2].count('-') == 0:
        clearField()
        print("Ничья")
        
    if isWin():
        print("You are win!")
        clearField()
        printfield()


