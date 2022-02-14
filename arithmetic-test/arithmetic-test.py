
import random
import sys

def isNumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def normalInput(text):
    while True:
        answer = input(text)
        if isNumber(answer):return answer
        else:print("Incorrect, try again")
    


level = normalInput("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
""")

if level != '1' and level != '2':
    print("Incorrect!")
    sys.exit()

mark = 0

for i in range(5):
   if level == "1":
       numb1 = random.randrange(2,10,1)
       numb2 = random.randrange(2,10,1)
       operations = random.randrange(1,4,1)

       if operations == 1:
           result = numb1 + numb2
           answer = normalInput(str(numb1) +" + "+str(numb2) + " = ")
           if int(answer) == result: mark = mark + 1

       if operations == 2:
           result = numb1 - numb2
           answer = normalInput(str(numb1) +" - "+str(numb2) + " = ")
           if int(answer) == result: mark = mark + 1

       if operations == 3:
           result = numb1 * numb2
           answer = normalInput(str(numb1) +" * "+str(numb2) + " = ")
           if int(answer) == result: mark = mark + 1
    
   if level == "2":
        numb = random.randrange(12,29,1)
        result = numb * numb
        answer = normalInput(str(numb) + " * " + str(numb) + " = ")
        if int(answer) == result: mark = mark + 1
      

print("Your mark is " + str(mark)+"/5" + ". Would you like to save the result? Enter yes or no.")
write = input()
if write == 'yes':
    name = input("What is your name? - ")
    file = open("result.txt","w")
    file.write(str(mark) + "/5" + ". Name - " + str(name))
    file.close()
    print("The results are saved in 'results.txt'.")


               



