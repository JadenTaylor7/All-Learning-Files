#Errors and Exceptions Homework
#Problem 1
#Handle the exception thrown by the code below by using try and except blocks.
#fix the TypeError
for i in ['a','b','c', 2, 5, 7, 'mary']:
    try:
        print(i**2)
    except TypeError:
        print("Oops, You are tyring to square a string value!")





print("\n")
#Problem 2
#Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
#fix the ZeroDivisionError
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Sorry bub, you are trying to divide by zero. Lemme change that.")
    y = (x + x)/x
    z = x/y
    print(z)
finally:
    print("All Done")


#Problem 3
#Write a function that asks for an integer and 
#prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    proceed = False
    while proceed == False:
        try:
            userInput = int(input("Give me an integer and I'll square it. "))
        except ValueError:
            print("That's not an integer. Try again")
            continue
        proceed = True
    squared = userInput**2
    print("{} squared is {}.".format(userInput, squared))

ask()

#Example:
#Input an integer: null
#An error occurred! Please try again!
#Input an integer: 2
#Thank you, your number squared is:  4
