import json

def investCash():
    money = input("How much money would you like to invest?: $")
    years = input("How many years do you want your money to grow?: ")
    print("\nCalculating value based on a 4% return compounded monthly...")
    #formula: A = P*(1+r/n)^(n*t)
    totalMoney = int(money) * (1+ .04/12)**(12*int(years))
    print("In {} years, your ${} will grow to be ${:1.2f}.".format(years,money,totalMoney))
    print("\nCalculating value based on a 7% return compounded monthly...")
    totalMoney2 = int(money) * (1+ .07/12)**(12*int(years))
    print("In {} years, your ${} will grow to be ${:1.2f}.".format(years,money,totalMoney2))


def investMoney(money = 0, years = 0):
    proceed = False
    while proceed == False:
        try:
            money = int(input("How much money would you like to invest?: $")) #money
        except ValueError:
            print("ERROR: Please enter a valid number")
            continue #prevents proceed from turning True
        proceed = True

    proceed = False
    while proceed == False:
        try: 
            years = int(input("How many years do you want your money to grow?: ")) #years
        except ValueError:
            print("ERROR: Please enter a valid number.")
            continue #prevents proceed from turning True
        proceed = True

    print("\n\n\nCalculating value based on 4%, 7% and 12% compounded monthly...")
    totalMoney4 = money * (1+ .04/12)**(12*years)
    totalMoney7 = money * (1+ .07/12)**(12*years)
    totalMoney12 = money * (1+ .12/12)**(12*years)
    totalList = [
        ["4%", "${:1.2f}".format(totalMoney4)],
        ["7%", "${:1.2f}".format(totalMoney7)],
        ["12%", "${:1.2f}".format(totalMoney12)]
    ]
    print("In {} years, your ${} will grow to an average of ${:1.2f}".format(years, money, totalMoney7))
    print("\nTotal Balance by growth rate (low, avg, high)")
    print(":  Interest rate  :  Total Balance (after {} yrs)".format(years))
    for item in totalList:
        #middle part will provide 12 spaces of distance no matter what (12 minus length of word)
        print(":  {}".format(item[0]), " "*(12-len(item[0])), " :  {}".format(item[1])) #" "is a space multiplied by 13, subtract however long the word is.
    #Compound interest for principal formula: A = P*(1+r/n)^(n*t)
    #future value of a series formula: TOTAL = A + (PMT *(((1+r/n)^(n*t) -1) / (r/n)) * (1 + r/n))
    #p = principal
    #r = annual interest rate (decimal)
    #n = number of times interest is compounded per year
    #t = time in years
    #PMT = monthly payment amount
    #A = future value of the investment/loan


def investMoneyContributions(money = 0, years = 0):
    proceed = False
    while proceed == False:
        try:
            money = int(input("How much money would you like to invest?: $")) #money
        except ValueError:
            print("ERROR: Please enter a valid number")
            continue #prevents proceed from turning True
        proceed = True

    proceed = False
    while proceed == False:
        try: 
            years = int(input("How many years do you want your money to grow?: ")) #years
        except ValueError:
            print("ERROR: Please enter a valid number.")
            continue #prevents proceed from turning True
        proceed = True

    proceed = False
    while proceed == False:
        try: 
            contribution = int(input("How much money will you contribute each month?: $")) #contribution
        except ValueError:
            print("ERROR: Please enter a valid number.")
            continue #prevents proceed from turning True
        proceed = True
    

    print("\n\n\nCalculating value based on 4%, 7% and 12% compounded monthly...")
    #totalMoney3 = money * (1+ .03/12)**(12*years)
    totalMoney4 = money * (1+ .04/12)**(12*years)
    totalMoney7 = money * (1+ .07/12)**(12*years)
    totalMoney12 = money * (1+ .12/12)**(12*years)
    #TotalContribute3 = totalMoney3 + (contribution *(((1 + .03/12)**(12*years) -1) / (.03/12)) * (1 + .03/12))
    TotalContribute4 = totalMoney4 + (contribution *(((1 + .04/12)**(12*years) -1) / (.04/12)) * (1 + .04/12))
    TotalContribute7 = totalMoney7 + (contribution *(((1 + .07/12)**(12*years) -1) / (.07/12)) * (1 + .07/12))
    TotalContribute12 = totalMoney12 + (contribution *(((1 + .12/12)**(12*years) -1) / (.12/12)) * (1 + .12/12))
    #Compound interest for principal formula: A = P*(1+r/n)^(n*t)
    #future value of a series formula: TOTAL = A + (PMT *(((1+r/n)^(n*t) -1) / (r/n)) * (1 + r/n))
    #p = principal
    #r = annual interest rate (decimal)
    #n = number of times interest is compounded per year
    #t = time in years
    #PMT = monthly payment amount
    #A = future value of the investment/loan
    totalList = [
        #["3%", "${:1.2f}".format(TotalContribute3)],
        ["4%", "${:1.2f}".format(TotalContribute4)],
        ["7%", "${:1.2f}".format(TotalContribute7)],
        ["12%", "${:1.2f}".format(TotalContribute12)]
    ]
    print("\nIn {} years, if you contribute ${} each month to your initial ${},\nyou will have an average of ${:1.2f}".format(years, contribution, money, TotalContribute7))
    print("\nTotal Balance by growth rate (low, avg, high)")
    print(":  Interest rate  :  Total Balance (after {} yrs)".format(years))
    for item in totalList:
        #middle part gives 12 spaces of distance no matter what (12 minus length of word)
        print(":  {}".format(item[0]), " "*(12-len(item[0])), " :  {}".format(item[1])) #" "is a space multiplied by 13, subtract however long the word is.

def investEatOutCash():
    print("\n\n\n\n\n\n\n\n\nBy choosing to pack a home lunch instead of eating out, you can invest the money you save from not eating out")
    print("(assuming the average home lunch is $3, and average eat out meal is $10).")
    proceed = False
    while proceed == False:
        try:
            meals = int(input("\nHow many eat out meals per month are you willing to give up?: ")) #meals
        except ValueError:
            print("ERROR: Please enter a valid number")
            continue #prevents proceed from turning True
        proceed = True

    proceed = False
    while proceed == False:
        try:
            years = int(input("\nHow many years before retirement (age 65)?: ")) #years
        except ValueError:
            print("ERROR: Please enter a valid number")
            continue #prevents proceed from turning True
        proceed = True


    #compound interest calculations from https://www.thecalculatorsite.com/finance/calculators/compound-interest-formula
    contribution = meals * 7
    totalMoney7 = contribution * (1+ .07/12)**(12*years)
    TotalContribute7 = totalMoney7 + (contribution *(((1 + .07/12)**(12*years) -1) / (.07/12)) * (1 + .07/12))

    print("\n\nBy choosing to eat home lunch instead of eat out for {} meals per month,".format(meals))
    print("\n\nyou'll save a total of ${:1.2f}.".format(TotalContribute7))
    print("\n\n\n")


def menu():
    print("Select an option")
    print("1: Invest some cash for fun")
    print("2: Invest for retirement")
    print("3: Invest your eating out money")
    userInput = input("Enter action 1-3 or back: ")
    validOptions = ["1","2","3","back"]
    while userInput not in validOptions:
        print("\nERROR: Please enter a valid number.\n")
        print("Select an option")
        print("1: Invest some cash for fun")
        print("2: Invest for retirement")
        print("3: Invest your eating out money")
        userInput = input("Enter action 1-3 or back: ")
    if userInput == "1":
        investMoney()
    elif userInput == "2":
        investMoneyContributions()
    elif userInput == "3":
        investEatOutCash()
    else: #user wants to go back
        pass





if __name__ == "__main__":
    #investCash()
    #investMoney()
    #investMoneyContributions()
    #investEatOutCash()
    menu()
