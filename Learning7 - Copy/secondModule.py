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


