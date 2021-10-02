import random

_words = ["JavaScript", "Java","Python", "Ruby"]
_rngWord = _words[random.randrange(4)]

print("Guess the word: " + _rngWord[0:len(_rngWord)-3]+"---")

if input().lower() == _rngWord.lower():
    print("You survived!")
else:
    print("You lost!")


