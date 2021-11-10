# Stage 3
import math

TYPE = input("""
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal: """)

if TYPE == "n":
        PRINCIPAL = input("Enter the loan principal: ")
        MONTHLY = input("Enter the monthly payment: ")
        INTEREST = input("Enter the monthly payment: ")
        i = (int(INTEREST))/(12*100)
        n = math.ceil(math.log( int(MONTHLY) / (int(MONTHLY) - i * int(PRINCIPAL)),1 + i))
        print("It will take " + str(math.floor(n/12)) + " years and " + str(math.ceil(n/12 - math.floor(n/12))+1) + " months to repay this loan!")

if TYPE == "a":
    PRINCIPAL = input("Enter the loan principal: ")
    PERIODS = input("Enter the number of periods: ")
    INTEREST = input("Enter the loan interest: ")

    i = 0.01
    num = (1 + i)**int(PERIODS)

    A = int(PRINCIPAL) * ((i * num) / (num - 1))
    
    print("Your monthly payment = " + str(A))

if TYPE == "p":
    print("")