# Write (or just say out loud to yourself) a brief description of all the following Object Types 
#and Data Structures we've learned about. You can edit the cell below by double clicking on it. 
#Really this is just to test if you know the difference between these, so feel free to just 
#think about it, since your answers are self-graded.



# Numbers: Any form of integer or float(decimal value)

# Strings: A grouping of characters in a text. Can be mixed numbers and letters.

# Lists: An ordered array of objects (basically an array in C++).

# Tuples: Same as lists, but values are immutable (not changeable).

# Dictionaries: An unordered set of pairs by key and value.




#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
#Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

myEquation = (((6 ** 3) /4.5) *2) + 12.2 -7.95
print("An equation that equals {}.".format(myEquation))


# Answer these 3 questions without typing code. Then type code to check your answer.

# What is the value of the expression 4 * (6 + 5)
    #Answer: 44

# What is the value of the expression 4 * 6 + 5 
    #Answer: 29

# What is the value of the expression 4 + 6 * 5
    #Answer: 34

expression1 = 4 * (6 + 5)
expression2 = 4 * 6 + 5
expression3 = 4 + 6 * 5
print("Expression one: {}".format(expression1))
print("Expression two: {}".format(expression2))
print("Expression three: {}".format(expression3))

 
# What is the type of the result of the expression 3 + 1.5 + 4?
    #Answer: float

guessingType = 3 + 1.5 +4
print(type(guessingType))

#What would you use to find a number’s square root, as well as its square?

# Square root: import math, math.sqrt(value). Another clever trick. 16 ** 0.5
# Square: root ** square

import math
squareRootSixteen = math.sqrt(16)
sixteenSquared = 16 ** 2
print("Square root of sixteen is: {s:1.0f}".format(s=squareRootSixteen)) #using precision
print("Sixteen squared is: {}".format(sixteenSquared))


#Strings
#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'

print(s[1])

#Reverse the string 'hello' using slicing:
reverseGreeting = s[-1] + s[-2] + s[-3] + s[-4] + s[-5]
revGreet = s[::-1]
print("hello backwards is " + reverseGreeting)
print("Another way to do it: " + revGreet)


#Given the string hello, give two methods of producing the letter 'o' using indexing.
# Method 1:
print(s[4])
# Method 2:
print(s[-1])



# Lists
# Build this list [0,0,0] two separate ways.
# Method 1:
someList = [0,0,0]
print("My list is {}".format(someList))
# Method 2:
list1 = [0]
list2 = [0,0]
listCombine = list1 + list2
print("Combined list: {}".format(listCombine))
# Method 3:
growList = [0]*100 #makes a list of 100 zeros
print("Large list: {}".format(growList))


#Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
print("Hello from list3: {}".format(list3[2][2])) #faster way

tempSet = list3[2]  #slower way
tempSet[2] = "goodbye"
list3[2] = tempSet
print(list3)


#Sort the list below:
list4 = [5,3,4,6,1]

list4.sort()
print(list4)



#Dictionaries
#Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
# Grab 'hello'
print("Grabbing hello: {}".format(d['simple_key']))

d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print("Grabbing hello: {}".format(d["k1"]["k2"]))

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print("Grabbing hello: {}".format(d["k1"][0]["nest_key"][1][0]))

#Grab hello
# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print("Grabbing hello: {}".format(d["k1"][2]["k2"][1]["tough"][2][0]))

#Can you sort a dictionary? Why or why not?
    #Answer: no, because it stores things by the key.



#Tuples
#What is the major difference between tuples and lists?
    #Answer: tuples are immutable(not changeable), while lists are.


#How do you create a tuple?
    #Answer: create it like so:
myTuple = (0,1,3,"something")
print(myTuple)
print(type(myTuple))



# Sets
# What is unique about a set?
    #Answer: a set is an unordered array of unique values. Can access at O(1) speed.

# Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(list5)
set5 = set(list5) #turning list into a set
print(set5) 
uniqueList5 = list(set5) #turning set back into a list
uniqueList5.sort() #sorting the list
print(uniqueList5)
print("We went from {l} to {ul}.".format(l=list5,ul=uniqueList5))




#Booleans
#What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# Answer before running cell
2 > 3
    #Answer: False
# Answer before running cell
3 <= 2
    #Answer: False
# Answer before running cell
3 == 2.0
    #Answer: False
# Answer before running cell
3.0 == 3
    #Answer: True
# Answer before running cell
4**0.5 != 2
    #Answer: False
#Final Question: What is the boolean output of the cell block below?

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
l_one[2][0] >= l_two[2]['k1']
    #Answer: False (3 != 4)
#Great Job on your first assessment!

