
#Function practice Exercises

# Warmup - these can be solved using basic comparisons and methods
# Level 1 - these may involve if/then conditional statements and simple methods
# Level 2 - these may require iterating over sequences, usually with some kind of loop
# Challenging - these will take some creativity to solve


#WARMUP SECTION: WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if 
#both numbers are even, but returns the greater if one or both numbers are odd
#Example: lesser_of_two_evens(2,4) --> 2
#Example: lesser_of_two_evens(2,5) --> 5
def lesser_of_two_evens(a,b):
    if ((a % 2 == 0) and (b % 2 == 0)):
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b
# Check
print(lesser_of_two_evens(2,4))
# Check
print(lesser_of_two_evens(2,5))

#easier way:
#    if ((a % 2 == 0) and (b % 2 == 0)):
#         return min(a,b)
#     else:
#         return max(a,b)

print("\n")
#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#Example: animal_crackers('Levelheaded Llama') --> True
#Example: animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(text):
    text = text.split()
    # print(text) #practice
    # print(text[0][0]) #practice
    # print(text[1][0]) #practice
    if text[0][0] == text[1][0]:
        return True
    else:
        return False

# Check
print(animal_crackers('Levelheaded Llama'))
# Check
print(animal_crackers('Crazy Kangaroo'))




print("\n")
#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#Example: makes_twenty(20,10) --> True
#Example: makes_twenty(12,8) --> True
#Example: makes_twenty(2,3) --> False
def makes_twenty(n1,n2):
    if (n1 + n2 == 20) or (n1 == 20) or (n2 == 20):
        return True
    else:
        return False

# Check
print(makes_twenty(20,10))
# Check
print(makes_twenty(12,8))
# Check
print(makes_twenty(2,3))




print("\n")
#LEVEL 1 PROBLEMS 11111111111111111111111111111111111111111111111111111111111111111111111111111111111111
#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
#Example: old_macdonald('macdonald') --> MacDonald

#Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    myList = []
    for i in range(len(name)):
        if i == 0 or i == 3:
            myList.append(name[i].upper())
        else:
            myList.append(name[i])
    #print(myList) #for testing
    str1 = ""
    name = str1.join(myList)
    return name
# Check
print(old_macdonald('macdonald'))
# Check
print(old_macdonald("bigboiMySumoGuy"))


print("\n")
#MASTER YODA: Given a sentence, return a sentence with the words reversed
#Example: master_yoda('I am home') --> 'home am I'
#Example: master_yoda('We are ready') --> 'ready are We'

#Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

#>>> "--".join(['a','b','c'])
#>>> 'a--b--c'

#This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

#>>> " ".join(['Hello','world'])
#>>> "Hello world"

def master_yoda(text):
    #putting into list
    splitMeLeggings = text.split()
    #print(splitMeLeggings) #for testing

    #reversing
    splitMeLeggings.reverse()
    #print("Reversed version: {}".format(splitMeLeggings)) #for testing

    #putting into string
    str1 = " "
    text = str1.join(splitMeLeggings)
    return text

# Check
print(master_yoda('I am home'))
# Check
print(master_yoda('We are ready'))




print("\n")
#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#Example: almost_there(90) --> True
#Example: almost_there(104) --> True
#Example: almost_there(150) --> False
#Example: almost_there(209) --> True

#NOTE: abs(num) returns the absolute value of a number

def almost_there(n):
    if n >= 190 and n <= 210:
        return True
    elif n >= 90 and n <= 110:
        return True
    else:
        print("Bro what the 'fff' your guess was way off")
        return False


# Check
print(almost_there(90))
# Check
print(almost_there(104))
# Check
print(almost_there(150))
# Check
print(almost_there(209))

#Absolute value way:
#return (abs(100-n) <= 10) or (abs(200-n) <= 10)



print("\n")
#LEVEL 2 PROBLEMS 222222222222222222222222222222222222222222222222222222222222222222222222222222
#FIND 33:
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

#Example: has_33([1, 3, 3]) → True
#Example: has_33([1, 3, 1, 3]) → False
#Example: has_33([3, 1, 3]) → False

def has_33(nums):
    daLength = len(nums)
    #print("This list is {} iterations long.".format(daLength)) #for testing
    for i,j in enumerate(nums):
        if i == 0: #if the first iteration, do nothing
            #only check forward
            pass
        elif i == (daLength -1): #if the last iteration, do nothing
            #print("The last iteration at {} is {}.".format(i,nums[i])) #for testing
            pass
        else:
            #checkbackward and forward
            if nums[i] == 3:
                if nums[i-1] == 3 or nums[i+1] ==3:
                    return True
            # print("nums -1 is: {}".format(nums[i-1])) #for testing
            # print("nums is: {}".format(nums[i])) #for testing
            # print("nums +1 is: {}".format(nums[i+1])) #for testing
    return False
            
# Check
print(has_33([1, 3, 3]))
# Check
#print("\n") #for testing
print(has_33([1, 3, 1, 3]))
# Check
#print("\n") #for testing
print(has_33([3, 1, 3]))
# Check
#print("\n") #for testing
print(has_33([2,1,3,65,4,2,3,1,4,2,8,3,2,9,0]))
# Check
#print("\n") #for testing
print(has_33([2,1,3,65,4,2,3,1,4,2,3,3,2,9,0]))


#Easier way:
#for i in range(0, len(nums)-1):
#   if nums[i] == 3 and nums[i+1] == 3:
#       return True
#
#return False


print("\n")
#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#Example: paper_doll('Hello') --> 'HHHeeellllllooo'
#Example: paper_doll('Mississippi') --> 'MMMiiissssssiiissssssiiippppppiii'
def paper_doll(text):
    text = str(text)
    listMe = []
    for i in range(len(text)):
        listMe.append(text[i])
        listMe.append(text[i])
        listMe.append(text[i])
        #print("Current list: {}".format(listMe)) #for testing

    str1 = ""
    text = str1.join(listMe)
    return text

# Check
print(paper_doll('Hello'))
# Check
print(paper_doll('Mississippi'))
# Check
print(paper_doll("Run!"))


#Easier way:
#result = ""
#
#for i in text:
#   result += i*3
#return result



print("\n")
#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
#If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum 
#(even after adjustment) exceeds 21, return 'BUST'
#Example: blackjack(5,6,7) --> 18
#Example: blackjack(9,9,9) --> 'BUST'
#Example: blackjack(9,9,11) --> 19
def blackjack(a,b,c):
    getSumGuns = a + b + c
    sumList = [a,b,c]
    if getSumGuns <= 21:
        #print("Your sum is: {}.".format(getSumGuns)) #for testing
        return getSumGuns
    elif getSumGuns > 21:
        for i in sumList:
            if i == 11:
                #i == 1 #probs not necessary for this.
                getSumGuns -= 10
                return getSumGuns
            else:
                pass
        if getSumGuns > 21:
            return "BUST"
    else:
        print("I'm a teapot.") #something wrong happened if this is accessed
        pass

# Check
print(blackjack(5,6,7))
# Check
print(blackjack(9,9,9))
# Check
print(blackjack(9,9,11))
# Check
print(blackjack(11,9,11))
# Check
print(blackjack(9,10,11))
# Check
print(blackjack(13,4,8))


#Other way:
#if sum([a,b,c]) <= 21:
#   return sum([a,b,c])
#elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
#   return sum([a,b,c])-10
#else:
#   return "BUST"


print("\n")
#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers 
#starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
#Return 0 for no numbers.
#Example: summer_69([1, 3, 5]) --> 9
#Example: summer_69([4, 5, 6, 7, 8, 9]) --> 9
#Example: summer_69([2, 1, 6, 9, 11]) --> 14
def summer_69(arr):
    cuteSummary = 0
    sixAlert = False
    for i in arr:
        if (i != 6) and (sixAlert == False):
            cuteSummary += i
            #print(cuteSummary) #for testing
        elif (i !=6) and (sixAlert == True): 
            if i == 9: #Check if number is a 9. Turn off sixAlert if so.
                sixAlert = False
                pass
            else:
                pass
        else: #it IS a six. Turn on sixAlert
            sixAlert = True
            pass
    return cuteSummary

# Check
print(summer_69([1, 3, 5]))
# Check
#print("\n") #for testing
print(summer_69([4, 5, 6, 7, 8, 9]))
# Check
#print("\n") #for testing
print(summer_69([2, 1, 6, 9, 11]))
# Check
#print("\n") #for testing
print(summer_69([2, 6, 4, 3, 2, 5, 9, 5, 1, 2, 4, 6, 8, 9, 1, 11]))
# Check
#print("\n") #for testing
print(summer_69([1,2,3,6,4,5]))



print("\n")
#CHALLENGING PROBLEMS   CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
#SPY GAME: 
#Write a function that takes in a list of integers and returns True if it contains 007 in order
#Example: spy_game([1,2,4,0,0,7,5]) --> True
#Example: spy_game([1,0,2,4,0,5,7]) --> True
#Example: spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(nums):
    firstZero = False
    secondZero = False
    firstSeven = False
    for i in nums:
        if firstZero == False:
            if i == 0:
                firstZero = True
                #print("First bady guy down.") #for testing
            else:
                pass
        elif secondZero == False:
            if i == 0:
                secondZero = True
                #print("Second bad guy down.") #for testing
            else:
                pass
        elif firstSeven == False:
            if i == 7:
                firstSeven = True #this finishes the search. Boss defeated. He go bye bye.
                #print("Final boss down. We win!") #for testing
                return True
            else:
                pass
        else:
            print("Something wrong happened. You shouldn't access this.")
    return False        
    
# Check
print(spy_game([1,2,4,0,0,7,5]))
# Check
#print("\n") #for testing
print(spy_game([1,0,2,4,0,5,7]))
# Check
#print("\n") #for testing
print(spy_game([1,7,2,0,4,5,0]))
# Check
#print("\n") #for testing
print(spy_game([1,0,2,7,4,5,0,0,3,2,5]))
# Check
#print("\n") #for testing
print(spy_game([1,7,2,0,4,5,7,7,3,5,8,7]))
# Check
#print("\n") #for testing
print(spy_game([40,36,32,0,33,20,21,0,22,15,14,7,3,2,1,12]))

#Easier way:
#code = [0,0,7,"x"]
#for i in nums:
#   if i == code[0]:
#       code.pop(0)
#
#return len(code) == 1



print("\n")
#COUNT PRIMES: Write a function that returns the number of prime numbers 
#that exist up to and including a given number
#Example: count_primes(100) --> 25

#By convention, 0 and 1 are not prime.

def count_primes(num): 
    potentialSuspects = num -1 #chosen range minus 1 because 1 isn't prime
    primeNumbas = [2]
    numPass = False
    for i in range(2,num +1,1): #checks numbers 2 - whatever range we choose
        numPass = False
        for j in primeNumbas:
            currentNumber = i #keeping track of our number outside of loop
            if numPass == False and i > j: #if still a suspect, and not dividing by something larger than itself
                divideTime = i % j
                #print(divideTime) #for testing
                if divideTime == 0:
                    numPass = True #no longer a suspect
                    #print("{} passes the test!".format(i)) #for testing
                    potentialSuspects -= 1
                    #print("Suspects left: {}".format(potentialSuspects)) # for testing
                else:
                    pass
            else:
                pass
        if numPass == False: #if statement not needed, but reduces compile time
            primeNumbas.append(i) #this part needed to check against new prime numbers
        else:
            pass
        #numPass is True if notprime, and False if it is prime    
        #print("{} is: {}".format(currentNumber,numPass)) #for testing
    
    print("List of Prime numbers: \n {}".format(primeNumbas)) #only if you wanna see what the prime numbers are
    print("Total prime number count:")
    return potentialSuspects

# Check
print(count_primes(100))
# Check
print(count_primes(150))
# Check
print(count_primes(1000))

#easier way to write it:
# primes = [2]
# for i in range(3, num + 1, 2): #iterating through every odd number makes compile time faster
#     for j in primes:
#         if i % j == 0:
#             break
#     else:
#         primes.append(i)
# return len(primes)


print("\n")
#PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
#Example: print_big('a')

# out:   *  
#       * *
#      *****
#      *   *
#      *   *
#HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line
# combinations of patterns. For purposes of this exercise, it's ok if your dictionary stops at "E".

def print_big(letter):
    if letter == "a" or letter == "A":
        print("\n")
        print("  *  ")
        print(" * * ")
        print("*****")
        print("*   *")
        print("*   *")
        print("*   *")
    elif letter == "b" or letter == "B":
        print("\n")
        print("**   ")
        print("* *  ")
        print("**   ")
        print("* *  ")
        print("*  * ")
        print("**   ")
    elif letter == "c" or letter == "C":
        print("\n")
        print("   **")
        print(" **  ")
        print("*    ")
        print("*    ")
        print(" **  ")
        print("   **")
    elif letter == "d" or letter == "D":
        print("\n")
        print("**   ")
        print("*  * ")
        print("*   *")
        print("*   *")
        print("*  * ")
        print("**   ")
    elif letter == "e" or letter == "E":
        print("\n")
        print("*****")
        print("*    ")
        print("***  ")
        print("*    ")
        print("*****")



    else:
        print("")

# Check
print_big('a')
# Check
print_big('b')
# Check
print_big('c')
# Check
print_big('d')
# Check
print_big('e')

