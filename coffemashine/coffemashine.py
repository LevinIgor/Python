
def printIng():
    print("The coffee mashine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(coffee) + " of coffee")
    print(str(cup) + " of disposable cups")
    print(str(money) + " of money")
    print()


money = 550
water = 400
milk = 540
coffee = 120
cup = 9

while True:

    print("Write action (buy, fill, take, remaining, exit):")
    action = input()

    if action == "b":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back:")
        buy =input()
        if buy == "1":
            if water - 250 > 0 and coffee - 16 > 0 and cup > 0:
                water = water - 250
                coffee = coffee - 16
                cup = cup -1
                money = money + 4
            else:
                print("Недостаточно ингредиентов")
        if buy == "2":
            if water -350 > 0 and milk - 75 > 0 and coffee - 20 > 0 and cup > 0:
                water = water - 350
                milk = milk - 75
                coffee = coffee - 20
                cup = cup -1
                money = money + 7
            else:
                print("Недостаточно ингредиентов")
        if buy == "3":
            if water - 200 > 0 and milk - 100 > 0 and coffee - 12 > 0 and cup > 0:
                water = water - 200
                milk = milk - 100
                coffee = coffee - 12
                cup = cup -1
                money = money + 6
            else:
                print("Недостаточно ингредиентов")
        if buy == "b":
            continue
    if action == "t":
        print("I gave you " + str(money))
        money = 0
    if action == "f":
        print("Write how many ml of water you want to add:")
        water = water + int(input())
        print("Write how many ml of milk you want to add:")
        milk = milk + int(input())
        print("Write how many grams of coffee beans you want to add:")
        coffee = coffee + int(input())
        print("Write how many disposable coffee cups you want to add:")
        cup = cup + int(input())
    if action == "r":
        printIng()
    if action == "e":
        break



