def diff_int():
    arr = []
    mp_cnt = PERIOD * 12
    rest = PRINCIPAL
    mp_real = PRINCIPAL / (PERIOD * 12.0)
    while mp_cnt != 0:
        mp = mp_real + (rest * PERCENT / 1200)
        arr.append(round(mp, 2))
        rest = rest - mp_real
        mp_cnt = mp_cnt - 1
    return arr, round(sum(arr), 2)


def ann_int():
    mp_cnt = PERIODS
    r = INTEREST / 1200.0
    ak = (r * (1 + r) ** mp_cnt) / (((1 + r) ** mp_cnt) - 1)
    mp = ANNUITY * ak
    total = mp * mp_cnt
    return round(mp, 2), round(total, 2)


# Stage 4
import math

TYPE = input("""
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
type "d" for different
 """)

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
    ANNUITY = float(input("Enter the annuity payment: ")) 
    PERIODS = int( input("Enter periods: "))
    INTEREST =float( input("Enter interest: ")) 
    month = ann_int()
    print("Month: " + str(round(month[0])))
   

if TYPE == "d":
    PRINCIPAL =int(input("Enter principal: "))
    PERIOD =int(input("Enter period: ")) /12
    PERCENT = int(input("Enter percent: "))
    months,total = diff_int()
    for i in range(len(months)):
        print("Month"+" " + str(i) + " : "+ str(months[i]))
    print("Overpayment = " + str(round(total-PRINCIPAL,2)))