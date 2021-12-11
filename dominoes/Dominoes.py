import random
import sys
import math
DOMINOES = [[2,5],[1,2],[3,6],[0,0],[0,2],[5,6],[3,5],[2,4],[3,4],[1,5],[0,4],[2,6],[3,3],[1,1],[1,4],[1,3],[2,3],[4,5],[2,2],[0,3],[0,6],[5,5],[4,4],[4,6],[0,1],[0,5],[1,6],[6,6]]
DOMINOES_copy = [[2,5],[1,2],[3,6],[0,0],[0,2],[5,6],[3,5],[2,4],[3,4],[1,5],[0,4],[2,6],[3,3],[1,1],[1,4],[1,3],[2,3],[4,5],[2,2],[0,3],[0,6],[5,5],[4,4],[4,6],[0,1],[0,5],[1,6],[6,6]]
dominoesField = []
currentTurn = ""

def setDominoes():
    dominoes = []
    while len(dominoes) !=7:
        RANDOM = random.randint(0, len(DOMINOES) - 1)
        dominoes.append(DOMINOES[RANDOM])
        DOMINOES.pop(RANDOM)
    dominoes.sort()
    return dominoes

def dominoSnake(dominoes):
    snake = [-1,-1]
    for i in dominoes:
        if (i[0] == i[1]):
            snake = i
    return snake

def addToStart(domino):
    dominoesField.insert(0, domino)
def addToEnd(domino):
    dominoesField.append(domino)

def computerMove():
    for i in range(len(computerDominoes)-1):
        if computerDominoes[i][0] == dominoesField[len(dominoesField)-1][1]:
            addToEnd(computerDominoes[i])
            computerDominoes.pop(i)
            return
        if computerDominoes[i][1] == dominoesField[0][0]:
            addToStart(computerDominoes[i])
            computerDominoes.pop(i)
            return
    if len(DOMINOES)>0:
        takeDominoes(computerDominoes)
    else:
        print("Вы выиграли")
        sys.exit()
    print("Компьютер взял кость из кучи")

def takeDominoes(e):
    rand = random.randint(0,len(DOMINOES)-1)
    e.append(DOMINOES[rand])
    print(DOMINOES[rand])
    DOMINOES.pop(rand)

playerDominoes,computerDominoes = setDominoes(),setDominoes()
playerSnake,computerSnake = dominoSnake(playerDominoes),dominoSnake(computerDominoes)

noneDominoes = [-1,-1]
while playerSnake == noneDominoes or computerSnake == noneDominoes:
    DOMINOES = DOMINOES_copy

    playerDominoes = setDominoes()
    computerDominoes = setDominoes()

    playerSnake = dominoSnake(playerDominoes)
    computerSnake = dominoSnake(computerDominoes)

if playerSnake>computerSnake:
    dominoesField.append(playerSnake)
    playerDominoes.pop(playerDominoes.index(playerSnake))
    currentTurn = "computer"
else:
    dominoesField.append(computerSnake)
    computerDominoes.pop(computerDominoes.index(computerSnake))
    currentTurn = "player"

print("============================================================================")
print(dominoesField)
while True:
    if currentTurn == "player":
        print("Field: "+str(dominoesField))
        print("Количество костей у компьютера: " + str(len(computerDominoes)))
        print("Количество костей в куче: "+str(len(DOMINOES)))
        for i in range(len(playerDominoes)):
            print(str(i+1)+":"+str(playerDominoes[i]))
        try:
            selectIndex = int(input("Введите номер кости: "))
            if math.fabs(selectIndex)-1 > len(playerDominoes)-1:
                print("Номер вышел за пределы")
            else:
                if selectIndex > 0:
                    if playerDominoes[selectIndex-1][0] == dominoesField[len(dominoesField)-1][1]:
                        addToEnd(playerDominoes[selectIndex-1])
                        playerDominoes.pop(selectIndex-1)
                        currentTurn = "computer"
                    else:
                        print("Невозможно установить! кость")
                elif selectIndex == 0:
                    if len(DOMINOES)>0:
                        takeDominoes(playerDominoes)
                    else:
                        print("Куча пуста")
                        if input("Для завершения нажмите 0 - ") == 0:
                            sys.exit()
                    currentTurn = "computer"
                elif selectIndex < 0:
                    if playerDominoes[selectIndex*-1-2][1] == dominoesField[len(dominoesField)-1][0]:
                        addToStart(playerDominoes[selectIndex*-1-1])
                        playerDominoes.pop(selectIndex*-1-1)
                        currentTurn = "computer"
                    else:
                        print("Невозможно установить кость!")
                
        except ValueError:
            print("Неверно введеные данные")  
    else:
        print("Ход компьютера")
        computerMove()
        currentTurn = "player"
    if len(playerDominoes) == 0:
        print("Вы выиграли")
        sys.exit()
    if len(computerDominoes) == 0:
        print("Компьютер выиграл")
        sys.exit()