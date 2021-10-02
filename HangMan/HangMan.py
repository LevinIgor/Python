import random

# Stage 1
print("""HANGMAN
The game will be available soon.""")


# Stage 2
print("Guess the word:")
if input() == "example":
    print("You survived!")
else:
    print("You lost!")


# Stage 3
_words = ["JavaScript","Java","Python","Ruby"]
print("Guess the word:")
if input().lower() == _words[random.randrange(4)].lower():
    print("You survived!")
else:
    print("You lost!")



