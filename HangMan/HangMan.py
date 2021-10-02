import random

_words = ["javascript", "java","python", "ruby"]
_rngWord = _words[random.randrange(4)]
_word = ""

for i in range(len(_rngWord)):
    _word = _word + "-"
print(_word)

for i in range(8):
    print("Input a letter:")
    _input = input()
    if  _input in _rngWord:
        for i in range(len(_rngWord)):
            if _input == _rngWord[i]:
                _word = _word[:i] + _input + _word[i+1:]
    print(_word)

print("""Thanks for playing!
We'll see how well you did in the next stage""")





