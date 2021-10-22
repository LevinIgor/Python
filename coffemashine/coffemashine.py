isWork = True
class CoffeMashine(object):
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.money = 550
        self.cup = 9
    
    def action(self, action):
        if action == "b":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back:")
            buy =input()
            if buy == "1":
                if self.water - 250 > 0 and self.coffee - 16 > 0 and self.cup > 0:
                    self.water = self.water - 250
                    self.coffee = self.coffee - 16
                    self.cup = self.cup -1
                    self.money = self.money + 4
                else:
                    print("Недостаточно ингредиентов")
            if buy == "2":
                if self.water -350 > 0 and self.milk - 75 > 0 and self.coffee - 20 > 0 and self.cup > 0:
                    self.water = self.water - 350
                    self.milk = self.milk - 75
                    self.coffee = self.coffee - 20
                    self.cup = self.cup -1
                    self.money = self.money + 7
                else:
                    print("Недостаточно ингредиентов")
            if buy == "3":
                if self.water - 200 > 0 and self.milk - 100 > 0 and self.coffee - 12 > 0 and self.cup > 0:
                    self.water = self.water - 200
                    self.milk = self.milk - 100
                    self.coffee = self.coffee - 12
                    self.cup = self.cup -1
                    self.money = self.money + 6
                else:
                    print("Недостаточно ингредиентов")
            if buy == "b":
                return self
        if action == "t":
            print("I gave you " + str(self.money))
            self.money = 0
        if action == "f":
            print("Write how many ml of water you want to add:")
            self.water = self.water + int(input())
            print("Write how many ml of milk you want to add:")
            self.milk = self.milk + int(input())
            print("Write how many grams of coffee beans you want to add:")
            self.coffee = self.coffee + int(input())
            print("Write how many disposable coffee cups you want to add:")
            self.cup = self.cup + int(input())
        if action == "r":
            self.printIng()
        if action == "e":
            global isWork
            isWork = False
 
    def printIng(self):
        print("The coffee mashine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.coffee) + " of coffee")
        print(str(self.cup) + " of disposable cups")
        print(str(self.money) + " of money")
        print()



coffeeMashine = CoffeMashine()
while isWork:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    coffeeMashine.action(action)
   







