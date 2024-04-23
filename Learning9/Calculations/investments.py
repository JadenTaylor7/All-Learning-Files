import pandas as pd
import random
import plotly
import plotly.graph_objects as go
from datetime import datetime

    #Compound interest for principal formula: A = P*(1+r/n)^(n*t)
    #future value of a series formula: TOTAL = A + (PMT *(((1+r/n)^(n*t) -1) / (r/n)) * (1 + r/n))
    #p = principal
    #r = annual interest rate (decimal)
    #n = number of times interest is compounded per year
    #t = time in years
    #PMT = monthly payment amount
    #A = future value of the investment/loan
class Investments():

    def __init__(self, money = 0, years = 0, yearList = [], df = "", PMT = 0):
        self.money = money
        self.years = years
        self.yearList = yearList
        self.df = df
        self.PMT = PMT #PMT = monthly payment amount
        

    def updateMoney(self, contributions):
        proceed = False
        while proceed == False:
            try:
                if contributions == "once":
                    self.money = int(input("How much money would you like to invest?: $")) #money
                    self.PMT = 0
                elif contributions == "monthly":
                    self.money = int(input("What will be your initial investment?: $")) #money
                    self.PMT = int(input("How much will you contribute each month?: $")) #monthly contribution
                else:
                    pass
            except ValueError:
                print("ERROR: Please enter a valid number")
                continue #prevents proceed from turning True
            proceed = True


    def updateYears(self):
        proceed = False
        while proceed == False:
            try: 
                self.years = int(input("How many years do you want your money to grow?: ")) #years
            except ValueError:
                print("ERROR: Please enter a valid number.")
                continue #prevents proceed from turning True
            proceed = True


    def investOnce(self):
        print("\nThis is investOnce")
        self.updateMoney("once")
        self.updateYears()

        print("\n\n\nCalculating value based on 4%, 7% and 12% compounded monthly...")
        count = datetime.now().year
        money4 = self.money
        money7 = self.money
        money12 = self.money
        self.yearList = [[count, money4, money7, money12]]
        for i in range(self.years):
            count += 1
            money4 = money4 * (1 + .04/12)**(12)
            money4 = round(money4,2) #round to two decimal places
            money7 = money7 * (1 + .07/12)**(12)
            money7 = round(money7,2) #round to two decimal places
            money12 = money12 * (1 + .12/12)**(12)
            money12 = round(money12,2)
            self.yearList.append([count, money4, money7, money12])
            #print(self.money) #for testing

        print("If you invested ${} today and left it alone, you would have ${:1.2f} in the year {}".format(self.yearList[0][1], money7, count))


        self.df = pd.DataFrame(self.yearList, columns=["Years", "Balance 4%", "Balance 7%", "Balance 12%"]) #columns is the titles for your columns
        #print(df)
        self.df.to_csv('balanceByYear.csv', index=False)

   

    def investRegular(self):
        print("\nThis is investRegular")
        self.updateMoney("monthly")
        self.updateYears()

        print("\n\n\nCalculating value based on 7% compounded monthly...")
        count = datetime.now().year
        monthlyContribute = self.PMT

        money4 = self.money
        yearlyContribute4 = monthlyContribute *((((1 + .04/12)**(12) -1) / (.04/12)) * (1 + .04/12)) #money added on each year
        monthlyMoney4 = 0

        money7 = self.money
        yearlyContribute7 = monthlyContribute *((((1 + .07/12)**(12) -1) / (.07/12)) * (1 + .07/12)) #money added on each year
        monthlyMoney7 = 0

        money12 = self.money
        yearlyContribute12 = monthlyContribute *((((1 + .12/12)**(12) -1) / (.12/12)) * (1 + .12/12)) #money added on each year
        monthlyMoney12 = 0

        self.yearList = [[count, money4, money7, money12]]
        for i in range(self.years):
            count += 1
            monthlyGrow4 = monthlyMoney4 * (1 + .04/12)**(12) #Interest on what's already in the pot
            monthlyMoney4 = monthlyGrow4 + yearlyContribute4 #the pot plue the new money added during the year
            money4 = money4 * (1 + .04/12)**(12) #principal
            totalMoney4 = money4 + monthlyMoney4 #principal plus monthly (A + M)
            totalMoney4 = round(totalMoney4,2) #round to two decimal places
            #print(totalMoney4) #for testing

            monthlyGrow7 = monthlyMoney7 * (1 + .07/12)**(12) #Interest on what's already in the pot
            monthlyMoney7 = monthlyGrow7 + yearlyContribute7 #the pot plue the new money added during the year
            money7 = money7 * (1 + .07/12)**(12) #principal
            totalMoney7 = money7 + monthlyMoney7 #principal plus monthly (A + M)
            totalMoney7 = round(totalMoney7,2) #round to two decimal places
            #print(totalMoney7) #for testing

            monthlyGrow12 = monthlyMoney12 * (1 + .12/12)**(12) #Interest on what's already in the pot
            monthlyMoney12 = monthlyGrow12 + yearlyContribute12 #the pot plue the new money added during the year
            money12 = money12 * (1 + .12/12)**(12) #principal
            totalMoney12 = money12 + monthlyMoney12 #principal plus monthly (A + M)
            totalMoney12 = round(totalMoney12,2) #round to two decimal places
            #print(totalMoney12) #for testing

            self.yearList.append([count, totalMoney4, totalMoney7, totalMoney12])



        print("If you invested ${} today and contributed ${} monthly, you would have ${:1.2f} in the year {}".format(self.yearList[0][1], self.PMT, totalMoney7, count))

        self.df = pd.DataFrame(self.yearList, columns=["Years", "Balance 4%", "Balance 7%", "Balance 12%"]) #columns is the titles for your columns
        #print(df)
        self.df.to_csv('balanceByYear.csv', index=False)        
        #Compound interest for principal formula: A = P*(1+r/n)^(n*t)
        #future value of a series formula: TOTAL = A + (PMT *(((1+r/n)^(n*t) -1) / (r/n)) * (1 + r/n))
        #future value of a series formula: TOTAL = A + M
        #p = principal
        #r = annual interest rate (decimal)
        #n = number of times interest is compounded per year
        #t = time in years
        #PMT = monthly payment amount
        #A = future value of the investment/loan
        #M = future value of monthly contributions



    def investEatOutCash(self):
        print("\nThis is investEatOutCash")
        homeLunchCost = 3
        print("\n\n\nYou can invest the money you save from packing a home lunch instead of eating out.")

        proceed = False
        while proceed == False:
            try:
                meals = int(input("\nHow many eat out meals per month are you willing to give up?: ")) #meals
                eatOutCost = int(input("How much do you spend when you eat out? $"))
            except ValueError:
                print("ERROR: Please enter a valid number")
                continue #prevents proceed from turning True
            proceed = True

        self.updateYears()
        self.money = 0 #reset this variable
        savePerMeal = eatOutCost - homeLunchCost
        self.PMT = (meals * savePerMeal) #calculate monthly contribution
        print("The monthly contribution will be: ${}".format(self.PMT)) #for testing

        print("\n\n\nCalculating value based on 7% compounded monthly...")
        count = datetime.now().year
        monthlyContribute = self.PMT

        money4 = self.money
        yearlyContribute4 = monthlyContribute *((((1 + .04/12)**(12) -1) / (.04/12)) * (1 + .04/12)) #money added on each year
        monthlyMoney4 = 0

        money7 = self.money
        yearlyContribute7 = monthlyContribute *((((1 + .07/12)**(12) -1) / (.07/12)) * (1 + .07/12)) #money added on each year
        monthlyMoney7 = 0

        money12 = self.money
        yearlyContribute12 = monthlyContribute *((((1 + .12/12)**(12) -1) / (.12/12)) * (1 + .12/12)) #money added on each year
        monthlyMoney12 = 0

        self.yearList = [[count, money4, money7, money12]]
        for i in range(self.years):
            count += 1
            monthlyGrow4 = monthlyMoney4 * (1 + .04/12)**(12) #Interest on what's already in the pot
            monthlyMoney4 = monthlyGrow4 + yearlyContribute4 #the pot plue the new money added during the year
            money4 = money4 * (1 + .04/12)**(12) #principal
            totalMoney4 = money4 + monthlyMoney4 #principal plus monthly (A + M)
            totalMoney4 = round(totalMoney4,2) #round to two decimal places
            #print(totalMoney4) #for testing

            monthlyGrow7 = monthlyMoney7 * (1 + .07/12)**(12) #Interest on what's already in the pot
            monthlyMoney7 = monthlyGrow7 + yearlyContribute7 #the pot plue the new money added during the year
            money7 = money7 * (1 + .07/12)**(12) #principal
            totalMoney7 = money7 + monthlyMoney7 #principal plus monthly (A + M)
            totalMoney7 = round(totalMoney7,2) #round to two decimal places
            #print(totalMoney7) #for testing

            monthlyGrow12 = monthlyMoney12 * (1 + .12/12)**(12) #Interest on what's already in the pot
            monthlyMoney12 = monthlyGrow12 + yearlyContribute12 #the pot plue the new money added during the year
            money12 = money12 * (1 + .12/12)**(12) #principal
            totalMoney12 = money12 + monthlyMoney12 #principal plus monthly (A + M)
            totalMoney12 = round(totalMoney12,2) #round to two decimal places
            #print(totalMoney12) #for testing

            self.yearList.append([count, totalMoney4, totalMoney7, totalMoney12])

        print("By packing home lunch {} meals per month and investing the savings, you would have ${:1.2f} in the year {}".format(meals ,totalMoney7, count))
        self.df = pd.DataFrame(self.yearList, columns=["Years", "Balance 4%", "Balance 7%", "Balance 12%"]) #columns is the titles for your columns
        self.df.to_csv('balanceByYear.csv', index=False)  
        

    def printDataframe(self):
        # if self.df == "":
        #     print("\nYou don't have a dataframe loaded")
        # else:
        print("\n\nPrincipal Investment: ${}".format(self.money))
        print("Monthly Contribution: ${}".format(self.PMT))
        print("Number of Years: {}".format(self.years))
        print("Your dataframe:")
        print(self.df)
        rothIRAThreshold = 6500
        if (self.PMT * 12) > rothIRAThreshold:
            overflow = (self.PMT * 12) - rothIRAThreshold
            print("""\nInvestment strategy: $6500 in Roth IRA, ${} in Traditional IRA annually, 
            mix of Mutual Funds and ETFs following S&P 500.""".format(overflow))
        else:
            print("\nInvestment strategy: Roth IRA Mutual Funds following S&P 500")




def investMenu(someCalculation):
    print("\nSelect investment strategy")
    print("1: One time investment")
    print("2: Regular contributions")
    print("3: Invest your eating out money")
    print("4: print dataframe")
    userInput = input("Enter action 1-4 or back: ")
    validOptions = ["1","2","3","4","back"]
    while userInput not in validOptions:
        print("\nERROR: Please enter a valid number.")
        print("\nSelect investment strategy")
        print("1: One time investment")
        print("2: Regular contributions")
        print("3: Invest your eating out money")
        print("4: print dataframe")
        userInput = input("Enter action 1-4 or back: ")
    if userInput == "1":
        someCalculation.investOnce()
        input ("\n(press enter to continue) ")
        investMenu(someCalculation)
    elif userInput == "2":
        someCalculation.investRegular()
        input ("\n(press enter to continue) ")
        investMenu(someCalculation)
    elif userInput == "3":
        someCalculation.investEatOutCash()
        input ("\n(press enter to continue) ")
        investMenu(someCalculation)
    elif userInput == "4":
        someCalculation.printDataframe()
        input ("\n(press enter to continue) ")
        investMenu(someCalculation)
    else: #user wishes to go back
        pass



newCalculation = Investments()
def begin(): #when getting called from retirement.py
    investMenu(newCalculation)



if __name__ == '__main__':
    newCalculation = Investments()
    investMenu(newCalculation)