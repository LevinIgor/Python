import random

_words = ["javascript", "java","python", "ruby"]
_rngWord = _words[random.randrange(len(_words))]
_word = ""

for i in range(len(_rngWord)):
    _word = _word + "-"
print(_word)

_points = 8

while _points > 0:
    _input = input("Input a letter:")
    if  _input in _rngWord and _input not in _word:
        for i in range(len(_rngWord)):
            if _input == _rngWord[i]:
                _word = _word[:i] + _input + _word[i+1:]
    else:
        _points = _points - 1

        if _input in _word:
            print("No improvements")
        else:
            print("That letter doesn't appear in the word")
    print(" ")
    print(_word)

    if "-" not in _word:
        print("""You guessed the word!
You survived!""")
        break


print(" ")
print("""Thanks for playing!
We'll see how well you did in the next stage""")





