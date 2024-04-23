class TheThirdModule():

    def __init__(self, name="", cash=0):
        self.name = name
        self.cash = cash
        

    def eatHealthy(self):
        print("Here {}, enjoy some brocoli with me.".format(self.name))
        print("Mmmmmm! I love me some good brocoli!")

    def yoinkCash(self):
        self.cash += 30
        print("You just yoinked $30 from someone.")
        print("You now have ${}.".format(self.cash))

    def changeName(self):
        if self.cash < 20:
            print("Sorry {}, it cost $20 to change your name".format(self.name))
            print("You'll have to yoink some cash from someone")
        else:
            print("That'll cost you $20 to change name. Do you accept?")
            userInput = input("(press 1 for yes, 2 for no) ")
            if (userInput == "1"):
                 self.cash -= 20
                 self.name = input("What would you like your new name to be?: ")
                 print("\nName changed to {}.".format(self.name))
            else:
                 print("Name not changed")
                 pass
        
        


def options(someUser):
        print("\nWhat would you like to do now?")

        optionsList = ["1: Eat healthy","2: Yoink some cash","3: Change name","4: Exit"]
        for i in optionsList:
            print(i)
        userOption = input("(Select a number 1-3): ")
        
        #handling invalid user input
        validOptions = ["1","2","3","4"]
        while userOption not in validOptions:
            print("Invalid input, try again.")
            print("\nWhat would you like to do now?")

            for i in optionsList:
                print(i)
            userOption = input("(Select a number 1-4): ")
        #end invalid user input

        if userOption == "1":
             print("\n")
             someUser.eatHealthy()
             options(someUser)
        elif userOption == "2":
             print("\n")
             someUser.yoinkCash()
             options(someUser)
        elif userOption == "3":
             print("\n")
             someUser.changeName()
             options(someUser)
        else:
             print("Good bye {}".format(someUser.name))
             
             
def start(someUser):
        print("\nYou are now accessing the thirdModule")
        someUser.name = input("What is your name? ")
        print("Thank you {} for your cooperation.".format(someUser.name))
        options(someUser)

newUser = TheThirdModule()
#start(newUser) #for testing, when running from this script

def accessGranted(): #function only accessed from a different .py script
    start(newUser)
             
        
