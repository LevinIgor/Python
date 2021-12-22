isWork = True
class CoffeMashine(object):
    def __init__(self):
        self.water = 4000
        self.milk = 5400
        self.coffee = 1200
        self.money = 5500
        self.cup = 90
        self.report = [0,0,0,0]
    
    def action(self, action):
        if action == "b":
            isBuy = True
            while isBuy:
                isBuy = False
                print("What do you want to buy? 1 - coffee, 2 - latte, 3 - cappuccino, back:")
                buy =input()
                if buy == "1":
                    if self.water - 250 > 0 and self.coffee - 16 > 0 and self.cup > 0:
                        # self.report[0]= self.report[0]+4
                        self.report[0]=self.report[0]+1
                        self.report[3]=self.report[3]+4
                        self.water = self.water - 250
                        self.coffee = self.coffee - 16
                        self.cup = self.cup -1
                        self.money = self.money + 4
                        print("Yes, i can make that amount of coffee")
                        answer = input("Хотите купить еще что-то? T/F  ")
                        if answer == "F":
                            return self
                        if answer == "T":
                            isBuy = True


                    else:
                        print("Недостаточно ингредиентов")
                if buy == "2":
                    if self.water -350 > 0 and self.milk - 75 > 0 and self.coffee - 20 > 0 and self.cup > 0:
                        self.report[1]=self.report[1]+1
                        self.report[3]=self.report[3]+7
                        self.water = self.water - 350
                        self.milk = self.milk - 75
                        self.coffee = self.coffee - 20
                        self.cup = self.cup -1
                        self.money = self.money + 7
                    else:
                        print("Недостаточно ингредиентов")
                if buy == "3":
                    if self.water - 200 > 0 and self.milk - 100 > 0 and self.coffee - 12 > 0 and self.cup > 0:
                        self.report[2]=self.report[2]+1
                        self.report[3]=self.report[3]+6
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
            try:
                self.water = self.water + int(input())
            except:
                print("Неверные данные, введеное кол-во 0")


            print("Write how many ml of milk you want to add:")
            try:
                self.milk = self.milk + int(input())
            except:
                print("Неверные данные, введеное кол-во 0")


            print("Write how many grams of coffee beans you want to add:")
            try:
                self.coffee = self.coffee + int(input())
            except:
                print("Неверные данные, введеное кол-во 0")


            print("Write how many disposable coffee cups you want to add:")
            try:
                self.cup = self.cup + int(input())
            except:
                print("Неверные данные, введеное кол-во 0")
                
            self.report =[0,0,0,0]
            
        if action == "r":
            self.printIng()
        if action == "e":
            global isWork
            isWork = False
        if action == "rep":
            print("Sell coffee: " + str(self.report[0]) + ".  Sell latte: " + str(self.report[1])+ ".  Sell cappuccino: " + str(self.report[2]) + ".  Total: " + str(self.report[3]))
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
   







