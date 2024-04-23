#overseer script
from Calculations import investments
import Calculations
from Calculations.investments import Investments
import pandas as pd

#needs work below
class Retirements(Investments):

    def __init__(self):
        self.searchDF = pd.dataframe()
#needs work above

def mainMenu():
    print("\nSelect an option")
    print("1: Invest for retirement")
    userInput = input("Enter action 1-1 or quit: ")
    validOptions = ["1","quit"]
    while userInput not in validOptions:
        print("\nERROR: Please enter a valid number.")
        print("\nSelect an option")
        print("1: Invest for retirement")
        userInput = input("Enter action 1-1 or quit: ")
    if userInput == "1": #invest for retirement
        investments.begin()
        print("Printing dataframe")
        mainMenu()
    else:
        print("Exiting code")



if __name__ == '__main__':
    mainMenu()
