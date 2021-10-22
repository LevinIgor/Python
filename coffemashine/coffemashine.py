import math

print("Write how many ml of water the coffee machine has:")
water = int(input())

print("Write how many ml of milk the coffee machine has:")
milk = int(input())

print("Write how many grams of coffee beans the coffee machine has:")
coffee =int(input()) 

print("Write how many cups of coffee you will need:")
count = int(input())

countMilk = milk/50
countWater = water/200
countCoffee = coffee/15
print("m:"+str(countMilk)+" w:"+str(countWater)+" c:"+str(countCoffee))
minimum =min(countMilk,countCoffee,countWater)


if(minimum==count):
    print("Yes, I can make that amount of coffee")
if minimum > count:
    print("Yes, I can make that amount of coffee (and even "+str(math.floor(minimum))+" more than that)")
if minimum < count:
    print("No, I can make only "+str(math.floor(minimum))+" cups of coffee")


