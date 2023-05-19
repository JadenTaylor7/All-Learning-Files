#overseer script
from FinancialStats import broke
from FinancialStats import millionaires
from FinancialCalculations import investmentCalculator
from FinancialStats.Sources import sourceLinks
import time

def begin():
    investmentCalculator.menu()
    input("\n(press enter to continue)")
    mainMenu()

def end():
    print("exiting code")

def mainMenu():
    print("Select an option")
    print("1: Financial calculation")
    print("2: Read financial findings")
    userInput = input("Enter action 1-2 or quit: ")
    validOptions = ["1","2","quit"]
    while userInput not in validOptions:
        print("\nERROR: Please enter a valid number.\n")
        print("Select an option")
        print("1: Financial calculation")
        print("2: Read financial findings")
        userInput = input("Enter action 1-2 or quit: ")
    if userInput == "1":
        investmentCalculator.menu()
        input("\n(press enter to continue)")
        mainMenu()
    elif userInput == "2":
        broke.printBrokeStats()
        millionaires.printMillionaireStats()
        input("(Press enter to see sources) ")
        sourceLinks.printSources()
        time.sleep(10)
        mainMenu()
    else:
        end()



if __name__ == "__main__":
    #probs just call functions here
    begin()
    
    

