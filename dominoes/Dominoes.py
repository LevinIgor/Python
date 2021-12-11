import random

DOMINOES = [[2,5],[1,2],[3,6],[0,0],[0,2],[5,6],[3,5],[2,4],[3,4],[1,5],[0,4],[2,6],[3,3],[1,1],[1,4],[1,3],[2,3],[4,5],[2,2],[0,3],[0,6],[5,5],[4,4],[4,6],[0,1],[0,5],[1,6],[6,6]]
DOMINOES_copy = [[2,5],[1,2],[3,6],[0,0],[0,2],[5,6],[3,5],[2,4],[3,4],[1,5],[0,4],[2,6],[3,3],[1,1],[1,4],[1,3],[2,3],[4,5],[2,2],[0,3],[0,6],[5,5],[4,4],[4,6],[0,1],[0,5],[1,6],[6,6]]

def setDominoes():
    dominoes = []
    while len(dominoes) !=7:
        RANDOM = random.randint(0, len(DOMINOES) - 1)
        dominoes.append(DOMINOES[RANDOM])
        DOMINOES.pop(RANDOM)
    dominoes.sort()
    return dominoes

def DominoSnake(dominoes):
    snake = [-1,-1]
    for i in dominoes:
        if (i[0] == i[1]):
            snake = i
    return snake



    

playerDominoes,computerDominoes = setDominoes(),setDominoes()
playerSnake,computerSnake = DominoSnake(playerDominoes),DominoSnake(computerDominoes)

noneDominoes = [-1,-1]
status=""
firstDominoes = []

if playerSnake == noneDominoes or computerSnake == noneDominoes:
    while playerSnake == noneDominoes or computerSnake == noneDominoes:
        DOMINOES = DOMINOES_copy

        playerDominoes = setDominoes()
        computerDominoes = setDominoes()

        playerSnake = DominoSnake(playerDominoes)
        computerSnake = DominoSnake(computerDominoes)

if playerSnake[0] > computerSnake[0]:
    playerDominoes.pop(playerDominoes.index(playerSnake))
    status = "computer"
    firstDominoes = playerSnake
else:
    computerDominoes.pop(computerDominoes.index(computerSnake))
    status = "player"
    firstDominoes = computerSnake

print("Stock size: " + str(len(DOMINOES)))
if status == "player":
    print("Computer pieces: " + str(len(computerDominoes)))
    print()
    print(firstDominoes)
else:
     print("Computer pieces: " + str(len(computerDominoes)))
     print()
     print(firstDominoes)

c = 1
print()
print("Your pieces:")
for i in playerDominoes:
    print(str(c) +":"+ str(i))
    c= c+1

if status == "player":
    print("Status: It's your turn to make a move. Enter your command.")
else:
    print("Status: Computer is about to make a move. Press Enter to continue...")





    



    

