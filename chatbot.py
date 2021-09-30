
print("""Hello! My name is KahovChatBot.
I was created in 2021.
Please, remind me your name.""")
print("What a great name you have, " + input() + "!")
print("""Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.""")

remainder3 = input()
remainder5 = input()
remainder7 = input()

print("Your age is " + str((int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105) +"; that's a good time to start programming!") 