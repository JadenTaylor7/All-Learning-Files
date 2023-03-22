#Functions and Methods Homework
#Complete the following questions: ____ Write a function that computes the volume of a sphere given its radius.

#The volume of a sphere is given as 4/3 pi r cubed
#Example: vol(2) --> 33.510321638291124
import math
def vol(rad):
    #print(math.pi) #for testing
    cubeIt = rad ** 3
    sphereVol = (4/3) * math.pi * cubeIt
    return sphereVol

# Check
print(vol(2))





print("\n")
#Write a function that checks whether a number is in a given range (inclusive of high and low)
#Example: ran_check(5,2,7) --> 5 is in the range between 2 and 7
def ran_check(num,low,high):
    if (num >= low) and (num <= high):
        print("{} is in the range between {} and {}.".format(num, low, high))
    else:
        print("Sorry bub, {} is out of range.".format(num))


# Check
ran_check(5,2,7)
# Check
ran_check(12,3,13)
# Check
ran_check(16,2,12)
# Check
ran_check(-3,-1,0.5)
# Check
ran_check(-1,-3,0.9)

#If you only wanted to return a boolean:
#Example: ran_bool(3,1,10) --> True
def ran_bool(num,low,high):
     if (num >= low) and (num <= high):
        return True
     else:
        return False
     
# Check
print(ran_bool(3,1,10))
# Check
print(ran_bool(12,3,13))
# Check
print(ran_bool(16,2,12))
# Check
print(ran_bool(-3,-1,0.5))
# Check
print(ran_bool(-1,-3,0.9))





print("\n")
#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output : 
#No. of Upper case characters : 4
#No. of Lower case Characters : 33

#HINT: Two string methods that might prove useful: .isupper() and .islower()

#If you feel ambitious, explore the Collections module to solve this problem!

def up_low(s):
    countLows = 0
    countHighs = 0
    s = str(s) #not needed, but nice
    for i in range(0,len(s),1):   #can do for loop as for i in s:
        if s[i].islower():    #can say if i.isupper():
            countLows += 1
        elif s[i].isupper():
            countHighs += 1
        else:
            pass
            #print("A Wild pokemon appeared! It's a: '{}'".format(s[i])) #for testing

    print("Number of lower case characters: {}".format(countLows))
    print("Number of upper case characters: {}".format(countHighs))


# Check
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
# Check
lol = 'I really just laughed out loud for the whole of us!'
up_low(lol)


print("\n")
#my personal challenge
def getTrolled(stuff):
    stuff = stuff.split()
    #print(len(stuff)) #for testing
    #stuff[0] = "Troll" #for testing
    for i in range(0,len(stuff),1):
        stuff[i] = "lo"
        stuff[0] = "Trol"
        stuff[len(stuff)-1] = "lol"

    #print(stuff) #for testing
    str1 = ""
    stuff = str1.join(stuff)
    return stuff

# Check
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(getTrolled(s))
# Check
lol = 'I really just laughed out loud for the whole of us!'
print(getTrolled(lol))





print("\n")
#Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
    lst = set(lst)
    return lst

# Check
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
# Check
print(unique_list([14,3,8,2,3,1,14,7,23,3,6,1,8,9,27,12,25,25,3,23,27,14,14,]))




print("\n")
#Write a Python function to multiply all the numbers in a list.
#Sample List : [1, 2, 3, -4]
#Expected Output : -24
def multiply(numbers):
    theTotal = 1
    for i in numbers:
        theTotal *= i
    #print("Your total is: {}".format(theTotal)) #for testing
    return theTotal

# Check
print(multiply([1,2,3,-4]))
# Check
print(multiply([1,5,7,23,0.5,-2,12,0.5,-1]))




print("\n")
#Write a Python function that checks whether a word or phrase is palindrome or not.
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.
#Example: palindrome('helleh') --> True

def palindrome(s):
    s = str(s)
    newS = s.replace(" ", "") #remove all spaces
    newS = newS.replace("!", "")
    newS = newS.lower()
    reversed = newS[::-1]
    #print(reversed) #for testing
    if newS == reversed:
        return True
    else:
        return False
    
    
    
    

# Check
print(palindrome('helleh'))
# Check
print(palindrome('halloween'))
# Check
print(palindrome('racar'))
# Check
print(palindrome("sit on a potato pan otis!"))
# Check
print(palindrome("Yummy boy!"))
# Check
print(palindrome("Too bad I hid a boot"))




print("\n")
#Hard:
#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog" --> True

#Hint: You may want to use .replace() method to get rid of spaces.

#Hint: Look at the string module

#Hint: In case you want to use set comparisons

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    #idea: remove spaces and make all lowercase, create a unique set of the letters, 
    # then sort them, then convert to string, then compare
    newS = str1.replace(" ", "")
    newS = newS.replace(",", "")
    newS = newS.replace(".", "")
    newS = newS.replace("!", "")
    newS = newS.replace("'", "")
    newS = newS.replace("?", "")
    #print(newS) #for testing
    newS = newS.lower()
    #print(newS) #for testing
    
    theSet = set(newS) #unique set of letters
    #print(theSet) #for testing

    sortedSet = sorted(theSet) #unique set sorted
    #print(sortedSet) #for testing

    str2 = ""
    sortedSet = str2.join(sortedSet) #convert to string
    #print(sortedSet) #for testing. Super helpful!
    #print(alphabet) #for testing
    if sortedSet == alphabet: #compare
        return True
    else:
        return False



# Check
string.ascii_lowercase
print(ispangram("The quick brown fox jumps over the lazy dog"))
# Check
string.ascii_lowercase
print(ispangram("I am going to eat burritos for the rest of my life!"))
# Check
string.ascii_lowercase
print(ispangram("The quick brown hogwarts foxV had zeal to meat dat juicy pboy"))
# Check
string.ascii_lowercase
print(ispangram("supercalifradulisticexpialidocious"))
# Check
string.ascii_lowercase
print(ispangram("alskdjfhgqpwoeirutyzmxncbvlololololo"))

