#validating user input

def enterPassword():
    thePassword = "Empty"

    while thePassword == "Empty":
        thePassword = input("Please enter the password (lard): ")

    while thePassword.lower() != "lard":
        thePassword = input("Wrong password, please try again: ")

    print("Congrats, you are now welcome to continue.")
    return thePassword


enterPassword()



print("Level two. The password is 3. You don't want to get this wrong.")
def turnToDigit():
    thePassword = ""

    while thePassword.isdigit() == False:
        thePassword = input("Enter password: ")

    return float(thePassword)
    
thePassword = turnToDigit()

def passwordPi(aPassword):
    if aPassword == 3:
        print("Congrats, you passed the test!")
    virusCount = 0
    while aPassword != 3 and virusCount < 30268:
        virusCount += 1
        print("Downloading Virus. {} viruses downloaded.".format(virusCount))

    print("You may now continue")
    return aPassword


passwordPi(thePassword)