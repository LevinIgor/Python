import random

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def input_number():
    while True:
        enter = input('Enter a number: ')
        if isNumber(enter):
            return float(enter)
        else:
            print("Invalid input.")


# Массив с числами
numbers = []

# Константы
PI = 3.141592653589793
E = 2.718281828459045
CONST = 333333333333333

# Выбор чисел для мат. операций
rand1 = random.randint(0, 4)
rand2 = random.randint(0, 4)
rand3 = random.randint(0, 4)

# Текст для принта
msgTextBefore = 'Number before change - '

# Заполненяем числами
for i in range(5):
    numbers.append(input_number())

# Числа до мат. операций
print(msgTextBefore, numbers)

# Выполняем мат. операции
numbers[rand1] = PI * numbers[rand1]
numbers[rand2] = E * numbers[rand2]
numbers[rand3] = CONST * numbers[rand3]

numbers[0] = numbers[rand1] + numbers[rand2]
numbers[4] = numbers[rand1] + numbers[rand2]

numbers[1] = numbers[rand1] - numbers[rand2]
numbers[3] = numbers[rand1] - numbers[rand2]

# Округляем
for i in range(5):
    numbers[i] = round(numbers[i],2) 

# Текст для вывода
inputString = f"\n Number 1 = {numbers[0]}; \n Number 1 = {numbers[0]}; \n Number 2 = {numbers[1]}; \n Number 3 = {numbers[2]}; \n Number 4 = {numbers[3]}; \n Number 5 = {numbers[4]}. \n"

# Вывод чисел после мат. операций
print(inputString)
