#Milestone project
#Based on my understanding of Python so far, create an interactive tic tac toe game
#Display, accept, validate, update

#Ideas for setup:
#Step 1: create player validate function (validates whether or not X or O)
#Step 2: create display function (shows the board)
#Step 3: create a user choice function (Let's the user choose what to do)
#Step 4: create a menu function (shows what the user can choose, including exit the game)
#Step 5: create a board updater (handles the game logic, sends input to display)
#Step 6: create a winner function (congratulates player if a player has won)
#Step 7: create play again function (clears board and starts over)
#Step 8: fix bugs, full game test cases.
#Idea: user choice will handle all the calls and functions inside it
#Thought: user choice function will have to be called at the very end, because it calls other functions
#That must be previously defined


#Step 1 enacted: Let player 1 decide if X or O. Choose player 2's letter based on player 1 answer.
def playerValidate(oneOrTwo):
    if oneOrTwo == 1: #if player 1 is choosing
        player = input("Player {}, do you want to be X or O? ".format(oneOrTwo))
    #if player 1 has already chosen, make player 2 the other option
    elif oneOrTwo == "X": 
        return "O"
    elif oneOrTwo == "O":
        return "X"
    else:
        print("Game encountered a problem. Please refresh the page.")
    
    #if player 1 is choosing
    playerReady = False
    while playerReady == False:
        if (player == "x") or (player == "X"):
            player = "X"
            return player
        elif (player == "o") or (player == "O"):
            player = "O"
            return player
        else:
            print("Please enter a valid input.")
            player = input("Player {}, do you want to be X or O? ".format(oneOrTwo))



#Step 2 enacted: displays default empty board, but can input X's or O's
def displayBoard(one=" ", two=" ", three=" ", four=" ", five=" ", six=" ", seven=" ", eight=" ", nine=" ",rules="N"):
    # two = "X" #for testing
    # three = "O" #for testing
    # five = "X" #for testing
    # seven = "O" #for testing
    # eight = "X" #for testing
    if rules == "N":  #this is displayed normally
        print("     |     |     ")
        print("  {}  |  {}  |  {}  ".format(seven, eight, nine))
        print("     |     |     ")
        print("-----|-----|-----")
        print("     |     |     ")
        print("  {}  |  {}  |  {}  ".format(four, five, six))
        print("     |     |     ")
        print("-----|-----|-----")
        print("     |     |     ")
        print("  {}  |  {}  |  {}  ".format(one, two, three))
        print("     |     |     ")

    else: #display this for instructions only
        print("          Column      ")
        print("       1     2     3  ")
        print(" Row      |     |     ")
        print("  1       |     |     ")
        print("          |     |     ")
        print("     -----|-----|-----")
        print("          |     |     ")
        print("  2       |     |     ")
        print("          |     |     ")
        print("     -----|-----|-----")
        print("          |     |     ")
        print("  3       |     |     ")
        input("          |     |        Press enter to continue ")



#Step 4 enacted: displays the menu that the user can choose from
def displayMenu():
    #displaying menu
    print("\n\n\n")
    print("        Menu        \n")
    print("Go Back (press enter)\n")
    print("Board Satus (press 'B')\n")
    print("Rows and Columns (press 'R')\n")
    selectMenu = input("Quit Game (press 'Q')\n")

    #input validation
    validOptions = ["","B","b","R","r","Q","q"]
    while selectMenu not in validOptions:
        print("Invalid response\n")
        print("        Menu        \n")
        print("Go Back (press enter)\n")
        print("Board Satus (press 'B')\n")
        print("Rows and Columns (press 'R')\n")
        selectMenu = input("Quit Game (press 'Q')\n")

    #do redirects here
    if (selectMenu == "B") or (selectMenu == "b"): #show the board
        displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
        input("Press enter to continue ")
        displayMenu()
        return True
    elif (selectMenu == "R") or (selectMenu == "r"): #Show rows and columns
        displayBoard("","","","","","","","","","Y")
        displayMenu()
        return True
    elif (selectMenu == "Q") or (selectMenu == "q"): #quit the game
        print("Exiting game. Thanks for playing!")
        exit()
    else:
        pass #go back



#Step 5 enacted: takes player information and updates the board
def boardUpdate(playerNumber, row, column):
    #should return opposite player number
    global box1
    global box2
    global box3
    global box4
    global box5
    global box6
    global box7
    global box8
    global box9
    if playerNumber == 1:
        global player1
        #each checks if slot is still empty by box == " "
        if row == 1 and column == 1 and box7 == " ": #assigning top left box a value
            box7 = player1 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(2)
            return True
        elif row == 1 and column == 2 and box8 == " " : #assigning top middle box a value
            box8 = player1 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(2)
            return True
        elif row == 1 and column == 3 and box9 == " ": #assigning top right box a value
            box9 = player1 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(2)
            return True
        elif row == 2 and column == 1 and box4 == " ": #assigning middle left box a value
            box4 = player1 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(2)
            return True
        elif row == 2 and column == 2 and box5 == " ": #assigning center box a value
            box5 = player1 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(2)
            return True
        elif row == 2 and column == 3 and box6 == " ": #assigning top right box a value
            box6 = player1 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(2)
            return True
        elif row == 3 and column == 1 and box1 == " ": #assigning bottom left box a value
            box1 = player1 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(2)
            return True
        elif row == 3 and column == 2 and box2 == " ": #assigning bottom middle box a value
            box2 = player1 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")  
            userChoice(2)
            return True
        elif row == 3 and column == 3 and box3 == " ": #assigning bottom right box a value.
            box3 = player1 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")  
            userChoice(2)
            return True
        else: #Player tried to overwrite other player's letter
            print("Bro, you cheated. Your turn gets skipped.")
            input("Press enter to continue ")
            lameCounter = 0
            while lameCounter < 20000:
                lameCounter += 1
                print("You cheated! Rubbing it in your face 20,000 times. {}".format(lameCounter))
            print("Okay, Player 2's turn now.")  
            userChoice(2)
            return True
    else: #player number == 2
        global player2
        #each checks if slot is still empty by box == " "
        if row == 1 and column == 1 and box7 == " ": #assigning top left box a value
            box7 = player2 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(1)
            return True
        elif row == 1 and column == 2 and box8 == " ": #assigning top middle box a value
            box8 = player2 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(1)
            return True
        elif row == 1 and column == 3 and box9 == " ": #assigning top right box a value
            box9 = player2 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(1)
            return True
        elif row == 2 and column == 1 and box4 == " ": #assigning middle left box a value
            box4 = player2 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(1)
            return True
        elif row == 2 and column == 2 and box5 == " ": #assigning center box a value
            box5 = player2 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(1)
            return True
        elif row == 2 and column == 3 and box6 == " ": #assigning top right box a value
            box6 = player2 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(1)
            return True
        elif row == 3 and column == 1 and box1 == " ": #assigning bottom left box a value
            box1 = player2 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(1)
            return True
        elif row == 3 and column == 2 and box2 == " ": #assigning bottom middle box a value
            box2 = player2 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(1)
            return True 
        elif row == 3 and column == 3 and box3 == " ": #assigning bottom right box a value
            box3 = player2 #inputs an X or O
            displayBoard(box1,box2,box3,box4,box5,box6,box7,box8,box9)
            input("Press enter to continue ")
            userChoice(1)
            return True 
        else:
            print("Bro, you cheated. Your turn gets skipped.")
            input("Press enter to continue ")
            lameCounter = 0
            while lameCounter < 20000:
                lameCounter += 1
                print("You cheated! Rubbing it in your face 20,000 times. {}".format(lameCounter))
            print("Okay, Player 1's turn now.")
            userChoice(1)
            return True

#Step 6 enacted: Detects winners and cheaters
def winnerFound(playerNumber):
    if playerNumber == 1: #switching to award correct player
        playerNumber = 2
    else: 
        playerNumber = 1

    winner = False
    global box1
    global box2
    global box3
    global box4
    global box5
    global box6
    global box7
    global box8
    global box9
    boxList = [box1,box2,box3,box4,box5,box6,box7,box8,box9]
    #print(boxList) #for testing
    emptyBox = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] #testing to see if board is empty
    if (winner == False) and (boxList == emptyBox): #game has just started
        return True
    elif winner == False: #checking different win options
        if (box5 == box4) and (box5 == box6) and (box5 != " "): #middle row the same
            again = input("Player {} wins! Play again ('Y' for yes, 'N' for no)? ".format(playerNumber))
            if again == "Y" or again == "y":
                playAgain()
                return True
            else:
                print("Thanks for playing!")
                exit()
        elif (box8 == box7) and (box8 == box9) and (box8 != " "): #top row the same
            again = input("Player {} wins! Play again ('Y' for yes, 'N' for no)? ".format(playerNumber))
            if again == "Y" or again == "y":
                playAgain()
                return True
            else:
                print("Thanks for playing!")
                exit()
        elif (box2 == box1) and (box2 == box3) and (box2 != " "): #bottom row the same
            again = input("Player {} wins! Play again ('Y' for yes, 'N' for no)? ".format(playerNumber))
            if again == "Y" or again == "y":
                playAgain()
                return True
            else:
                print("Thanks for playing!")
                exit()
        elif (box5 == box8) and (box5 == box2) and (box5 != " "): #middle column the same
            again = input("Player {} wins! Play again ('Y' for yes, 'N' for no)? ".format(playerNumber))
            if again == "Y" or again == "y":
                playAgain()
                return True
            else:
                print("Thanks for playing!")
                exit()
        elif (box4 == box7) and (box4 == box1) and (box4 != " "): #left column the same
            again = input("Player {} wins! Play again ('Y' for yes, 'N' for no)? ".format(playerNumber))
            if again == "Y" or again == "y":
                playAgain()
                return True
            else:
                print("Thanks for playing!")
                exit()
        elif (box6 == box9) and (box6 == box3) and (box6 != " "): #right column the same
            again = input("Player {} wins! Play again ('Y' for yes, 'N' for no)? ".format(playerNumber))
            if again == "Y" or again == "y":
                playAgain()
                return True
            else:
                print("Thanks for playing!")
                exit()
        elif (box5 == box7) and (box5 == box3) and (box5 != " "): #left diagonal the same
            again = input("Player {} wins! Play again ('Y' for yes, 'N' for no)? ".format(playerNumber))
            if again == "Y" or again == "y":
                playAgain()
                return True
            else:
                print("Thanks for playing!")
                exit()
        elif (box5 == box9) and (box5 == box1) and (box5 != " "): #right diagonal the same
            again = input("Player {} wins! Play again ('Y' for yes, 'N' for no)? ".format(playerNumber))
            if again == "Y" or again == "y":
                print("Excuse me, I just farted. Anyways, moving on.\n")
                playAgain()
                return True
            else:
                print("Thanks for playing!")
                exit()
        #if all squares filled, tie game
        elif (box1 != " ") and (box2 != " ") and (box3 != " ") and (box4 != " ") and (box5 != " ") and (box6 != " ") and (box7 != " ") and (box8 != " ") and (box9 != " "):
            again = input("Tie game. Jesus still loves you.\nPlay again ('Y' for yes, 'N' for no)? ".format(playerNumber))
            if again == "Y" or again == "y":
                playAgain()
                return True
            else:
                print("Thanks for playing!")
                exit()
        else:
            return True #no winner yet. Game consinues
        
    else:
        print("Something went wrong. Please restart game.")
        return True


#Step 7: start game over if players want to play again. Clears board and starts over.
def playAgain():
    #players select marker type
    player1 = playerValidate(1) #player 1 decides X or O
    print("Awesome!\n")
    player2 = playerValidate(player1) #player 2 given letter based on player 1 answer.
    print("Player 1 will be {}'s, and Player 2 will be {}'s.".format(player1,player2))
    input("Press enter to continue ")

    #clear the board
    global box1
    global box2
    global box3
    global box4
    global box5
    global box6
    global box7
    global box8
    global box9
    box1 = " "
    box2 = " "
    box3 = " "
    box4 = " "
    box5 = " "
    box6 = " "
    box7 = " "
    box8 = " "
    box9 = " "

    #begin the game
    displayBoard()
    userChoice(1)



#Step 3 enacted: Takes user input, and redirects to other functions based on input
#NOTE: Because this calls other functions, it must be at the end.
def userChoice(oneOrTwo):
    winnerFound(oneOrTwo) #checks if there is a winner
    print("Player {}'s turn (press 'M' for menu):".format(oneOrTwo))
    playerSelectRow = input("Choose a row, 1, 2 or 3: ")
    

    #answer validation (menu or row)
    validOptions = ["M","m","1","2","3"]
    while playerSelectRow not in validOptions:
        print("Invalid response")
        print("Player {}'s turn (press 'M' for menu):".format(oneOrTwo))
        playerSelectRow = input("Choose a row, 1, 2 or 3: ")


    #do redirects here (row)
    if playerSelectRow == "M" or playerSelectRow == "m": #player chose menu
        displayMenu()
        userChoice(oneOrTwo) #recursively calls itself after viewing menu
        return True
    elif playerSelectRow == "1" or playerSelectRow == "2" or playerSelectRow == "3": #player chose column
        playerSelectRow = int(playerSelectRow)
        #print(type(playerSelectRow)) #for testing
        playerSelectCol = input("Choose a column, 1, 2 or 3: ")
        #prompts player to select a column
    else:
        print("Something went wrong. Please restart the game.")


    #answer validation (menu or column)
    while playerSelectCol not in validOptions:
        print("Invalid response")
        playerSelectCol = input("Choose a column, 1, 2 or 3: ")

    
    #final redirects (column)
    if playerSelectCol == "M" or playerSelectCol == "m": #player chose menu
        displayMenu()
        userChoice(oneOrTwo) #recursively calls itself after viewing menu
        return True
    elif playerSelectCol == "1" or playerSelectCol == "2" or playerSelectCol == "3": #player chose column
        playerSelectCol = int(playerSelectCol)
        #print(type(playerSelectCol)) #for testing
        boardUpdate(oneOrTwo, playerSelectRow, playerSelectCol)
        return True #TODO change this
        #goes to board update function
    else:
        print("Something went wrong. Please restart the game.")

    




#Functions above this line, main calls below this line -------------------------------------------------------------

#Part 1: Pick players
print("Welcome to tic tac toe!")
player1 = playerValidate(1) #player 1 decides X or O
print("Awesome!\n")
player2 = playerValidate(player1) #player 2 given letter based on player 1 answer.
print("Player 1 will be {}'s, and Player 2 will be {}'s.".format(player1,player2))
input("Press enter to continue ")

#Part 2: Rules and instructions
print("Here is the board.")
displayBoard()
input("Press enter to continue ")

hearRules = input("Would you like to hear the rules? Y or N ") #player can skip rules or not
ruleCheck = ["Y","y","N","n"]
while hearRules not in ruleCheck: #check if valid response
    print("Invalid response")
    hearRules = input("Would you like to hear the rules? Y or N ")

if hearRules == "Y" or hearRules == "y":
    #player wants to hear rules. Explain it in here.
    print("\n")
    print("On each player's turn, you will be prompted to select a row, then a column.")
    print("Rows and columns are as follows:")
    input("Press enter to continue ")
    displayBoard("","","","","","","","","","Y")
    print("Choose your row by pressing 1, 2 or 3, then press enter.")
    print("Do the same with columns.")
    input("Press enter to continue ")
    print("\n\n\n\n\n\n\nGet three X's or three O's in a line to win. Simple!\n")
    print("At any time during your turn, you may press 'M', then enter to see the menu.\n")
    print("The menu allows you to see board status, display rows and columns, or quit the game.\n")
    input("Press enter to continue ")
    print("\n\n\n\nThat's all the rules.")

    
else:
    print("skipping rules\n\n\n\n")



print("Let's play!\n\n\n")

#Part 3: setting up global variables
box1 = " "
box2 = " "
box3 = " "
box4 = " "
box5 = " "
box6 = " "
box7 = " "
box8 = " "
box9 = " "
#players now stay in userChoice function for rest of game
displayBoard()
userChoice(1)

#Steb 8 enacted: Board fully functional, prevented cheaters from overwriting a filled space.
#One hidden easter egg.





