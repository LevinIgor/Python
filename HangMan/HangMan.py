import random

def replaceDash(_inputChar, _randomWord, _dashWord):
    for i in range(len(_randomWord)):
        if _inputChar == _randomWord[i]:
            _dashWord =  _dashWord[:i] + _inputChar + _dashWord[i+1:]
    return _dashWord

def isNormalInput(_inputChar):
    if len(_inputChar) > 1:
        print("You should input a single letter.")
        return False
    
    if _inputChar.isupper():
        print("Please enter a lowercase English letter.")
        return False
    return True

def isWin(_dashWord):
    if "-" not in _dashWord:
        print("""You guessed the word!
You survived!""")
        return True
    else:
        return False



while True:
    print("")
    _menu = input("Type 'play' to play the game, 'exit' to quit:")

    if _menu == "play":
        _words = ["javascript", "java","python", "ruby"]
        _randomWord = _words[random.randrange(len(_words))]
        _dashWord = ""
        _points = 8
        _inputChars = ""


        for i in range(len(_randomWord)):
            _dashWord = _dashWord + "-"
        print(_dashWord)  

        while _points > 0:
            _inputChar = input("Input a letter:")

            if isNormalInput(_inputChar):

                if _inputChar in _dashWord:
                    print("No improvements")

                if _inputChar not in _randomWord:
                    print("That letter doesn't appear in the word")
                

                if  _inputChar in _randomWord and _inputChar not in _dashWord:
                    _dashWord = replaceDash(_inputChar,_randomWord,_dashWord)
            
                if _inputChar not in _randomWord and _inputChar not in _inputChars:
                    _points = _points - 1

                if _inputChar in _inputChars and _inputChar not in _randomWord:
                    print("You've already guessed this letter.")
                _inputChars = _inputChars + _inputChar

            print(" ")
            print(_dashWord)
            
            if isWin(_dashWord):
                break

        print(" ")
        print("""Thanks for playing!
We'll see how well you did in the next stage""")
    elif _menu == "exit":
        print("Ok(")
        break
    