# Stage 2

import math


PRINCIPAL = input("Enter the loan principal:")
TYPE = input("""What do you want to calculate?
type 'm' - for number o monthly payments
type 'p' - for the monthly payment: """)


if TYPE == "m":
    PAYMENT = input("Enter the monthly payment: ")
    print("It will take " + str(math.ceil(int(PRINCIPAL)/int(PAYMENT))) + " months to repay the loan ")

if TYPE == "p":
     MONTHLY = input("Enter the number of months: ")
     if int(PRINCIPAL)/int((MONTHLY)) == math.ceil(int(PRINCIPAL)/int((MONTHLY))):
         print("Your monthly payment = " + str(int(PRINCIPAL)/int((MONTHLY))))
     else:
         print("Your monthly payment = " + str(math.ceil(int(PRINCIPAL)/int((MONTHLY)))) + " and the last payment = " + str(int(PRINCIPAL)-(math.ceil(int(PRINCIPAL)/(math.ceil(int(PRINCIPAL)/int(MONTHLY))))-1) * math.ceil(int(PRINCIPAL)/int(MONTHLY))))