

# Stage 1
print("""Hello! My name is KahovChatBot.
I was created in 2021.
Please, remind me your name.""")


# Stage 2
print("What a great name you have, " + input() + "!")


# Stage 3
print("""Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.""")
remainder3 = input()
remainder5 = input()
remainder7 = input()
print("Your age is " + str((int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105) +"; that's a good time to start programming!") 


# Stage 4
print("Now I will prove to you that I can count to any number you want.")
for i in range(int(input())+1):
    print(str(i)+" !")
print("Completed, have a nice day!")


