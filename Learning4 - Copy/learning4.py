from random import shuffle
import random

#functions
def test_function(name="George Clooney"):
    '''
    This section describes what the function does.
    Neat isn't it?
    '''
    print("Good morning "+name+".")
    print("Oof, it's too early, I'm going back to bed.")


test_function("Pedro")
#userChoose = input("What's your name? ")
#test_function(userChoose)
test_function()



#more complex function
def divisible(someNumbers):
    counter2 = 0
    counter3 = 0
    for i in someNumbers:
        if i % 2 == 0 and i % 3 == 0:
            print("{} is divisible by 2 and 3.".format(i))
            counter2 += 1
            counter3 += 1
        elif i % 2 == 0:
            print("{} is divisible by 2.".format(i))
            counter2 += 1
        elif i % 3 == 0:
            print("{} is divisible by 3.".format(i))
            counter3 += 1
        else:
            print("{} is not divisible by 2 or 3.".format(i))
    
    print("There are {} numbers divisible by 2, and {} numbers divisible by 3.".format(counter2,counter3))

spicyRange = []      
for i in range(0,21,1):
    spicyRange.append(i)
print(spicyRange)


divisible(spicyRange)
print("\n")

#checking for top 3 most expensive products
tupleToUnpack = [
    ("Sweet Dreams Sample", 0.75),
    ("Sweet Dreams Bottle", 17.5),
    ("DoubleX", 56.00),
    ("Protien Powder", 36.00),
    ("Protien Shakes", 44.25),
    ("Protien shake single", 3.75),
    ("MTG Deck", 27.00)
    ]

def topThree(products):
    mostExpensive = 2
    firstPlace = ""
    secondExpensive = 1
    secondPlace = ""
    thirdExpensive = 0
    thirdPlace = ""

    for item,cost in products:
        if cost > mostExpensive:
            #shift all the items down before crowning new leader
            thirdPlace = secondPlace
            secondPlace = firstPlace
            thirdExpensive = secondExpensive
            secondExpensive = mostExpensive
            #crown new leader
            mostExpensive = cost
            firstPlace = item

        if cost < mostExpensive and cost > secondExpensive:
             #shift all the items down before crowning new leader
            thirdPlace = secondPlace
            thirdExpensive = secondExpensive
            #crown second leader
            secondExpensive = cost
            secondPlace = item
        if cost < secondExpensive and cost > thirdExpensive:
            thirdExpensive = cost
            thirdPlace = item

    print("In first place, we have {p} at ${c}.".format(c = mostExpensive, p = firstPlace))
    print("Second place is {p} at ${c}.".format(c = secondExpensive, p = secondPlace))
    print("And in Third place, we have {p} at ${c}.".format(c = thirdExpensive, p = thirdPlace))
    return [(firstPlace,mostExpensive),(secondPlace,secondExpensive),(thirdPlace,thirdExpensive)]


first,second,third = topThree(tupleToUnpack)
print(third[0])
print(second[0])
print(first[0])



#assigning a library function to a variable
numbas = [0,1,2,3,4,5,6,7,8,9,10,11,12]
#result = shuffle(numbas) #THIS DOESN'T WORK

def cupidShuffle(someList):
    shuffle(someList)
    return(someList)

cupidShuffle(numbas)
print(numbas)



#creating a gambling machine with multiple functions
def randomGenerator():
    num = random.randrange(1,10)
    return num


#print(randomGenerator()) #testing function


def createWheel():
    someList = []
    someList.append(randomGenerator())
    someList.append(randomGenerator())
    someList.append(randomGenerator())
    return someList

#print(createWheel()) #testing function

def testYourLuck(money):
    wheel = createWheel()
    money -= 1
    if money > 0:
        if (wheel[0] == wheel[1]) and (wheel[1] == wheel[2]) and (wheel[0] == 7):
            money += 200
            print("{} Jacpot! You win $200! Money left: ${}.".format(wheel,money))
            return money
        elif (wheel[0] == wheel[1]) and (wheel[1] == wheel[2]):
            money += 30
            print("{} Triples. You win $30! Money left: ${}.".format(wheel,money))
            return money
            
        elif ((wheel[0] == (wheel[1] or wheel[2])) or (wheel[1] == wheel[2])):
            money += 1.5
            print("{} Doubles. You win $1.50. Money left: ${}.".format(wheel, money))
            return money
            
        else:
            print("{} You lose. Money left: ${}.".format(wheel,money))
            return money
    else:
        print("You have no money left. Gambling sucks.")    


myMoney = 200
numAttempts = []
for i in range(0,600,1):
    numAttempts.append(i)
for i in numAttempts:
    if myMoney > 230:
        break
    else:
        myMoney = testYourLuck(myMoney)



#*args
def getSum(*args): #accounts for any number of arguments
	return sum(args)

print(getSum(1,5,4,2,3))
print(getSum(3,1))



#**kwargs
def findBook(**kwargs):
    print(kwargs)
    if "bookOfMormon" in kwargs:
        print("Nice, you got the Book of Mormon!")
    else:
        print("You are missing a very important book")

findBook(oldTestament = "old Jerusalem", bookOfMormon = "old America")


#*args and **kwargs together
def randomStuff(*args,**kwargs):
    print(args[1], kwargs["bookOfMormon"])

randomStuff(1,4,7,2,0,bookOfMormon="old America", urMom="awesome")


#function that returns a string where every even letter is uppercase
#every odd letter is lowercase
myString = "GassyBoi"
for i in enumerate(myString):
    print(i)

def myFunkyChicken(someString):
    someString = list(someString)
    for i,j in enumerate(someString):
        if i % 2 == 0:
            someString[i] = j.upper()
            #print(j)
        else:
            someString[i] = j.lower()
            #print(j)
    print(someString)
    str1 = ""
    someString = str1.join(someString)
    print(type(someString))
    print(someString)
    return someString

myString = myFunkyChicken(myString)
print(myString)


#easier solution to the one above
# def myfunc(x):
#     out = []
#     for i in range(len(x)):
#         if i%2==0:
#             out.append(x[i].lower())
#         else:
#             out.append(x[i].upper())
#     return ''.join(out)