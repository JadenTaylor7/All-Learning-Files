print('hello world')
print('new')
#writing comments


print(2+1)
print(7/4)
print(7 % 4)
print(2 ** 3) #2 to the power of 3
print((2 + 10) * (10 + 3))
print(0.1+0.2-0.3) #why this doesn't equal 0 check out: https://docs.python.org/2/tutorial/floatingpoint.html

#creating variables
a = 2
a = 10
print(a +a)
a = a + a
print(a)
print(type(a)) # tells you what type this is
b = 3

myIncome = 500
taxRate = 0.14
taxTotal = myIncome * taxRate
print("Total taxes comes to",taxTotal)
print('Total taxes comes to',taxTotal)


print("I'm going on a run")
print("hello \nworld")
print("tab\ttab\ttab")

print("Using length function...",len("supercalifradulisticexpialidocious"))



#string indexing
someString = "Good morning!"
print(someString)
print(someString[0])
print(someString[8])
print(someString[-1])
print(someString[-2])

#string slicing
print(someString[0:4])
print(someString[3:7])
print(someString[3:])
print(someString[:6])
newString = "abcdefghijk"
print(newString[3:6]) #should grab def
print(newString[ :2],newString[1])

#stepsize
print(someString[::2])
codedMessage = "Dfeocaoldpejd"
print(codedMessage[::2]) #prints Decoded
print(someString[::-1])

#Concatenating
name = "Sam"
lastLetters = name[1:]
print("p"+lastLetters)
Greeting = "Good morning"
print(Greeting+" "+name)
Greeting = Greeting + " " + name
print(Greeting)
print(Greeting * 5)

#Using string library
print(Greeting.lower())
print(Greeting.upper())
print(Greeting.split())
print(Greeting.split("o"))
#creating a list
happy = Greeting.split()
print(happy)
print(happy[0])
print(type(happy))
print(happy[1])


#.format method
name = "Sam"
name2 = "George"
print("Hello {}, my name is {}. How are you?".format(name, name2))
print("Hello {1}, my name is {0}. Thanks for asking.".format(name, name2))

pi = 3.1415926535
print ("The number pi to 3 decimals is {p:1.3f}".format(p =pi))
#format literal method
print(f"Hello {name}, my name is {name2}. How are you?")


#lists!
firstList = [1,2,3]
secondList = [4,5,6]
print(firstList + secondList)
firstList[0] = "Got eem!" #changes first element
print(firstList)
firstList.append(12)
print(firstList)
firstList.insert(1,18)
print(firstList)



#dictionaries
myDictionary = {
    "first":"George Washington",
    "second":"John Adams",
    "third":"Thomas Jefferson",
    "fourth":"James Madison"
}

print(myDictionary["first"])
print("The first president of the US is {}".format(myDictionary["first"]))


usernamesAndPasswords = {
    "jtjadent@gmail.com":1234,
    "jadent6@byu.edu":"happypanda3",
    "taylorbros7@gmail.com":19587367
}
print("Password for jtjadent@gmail.com: {}".format(usernamesAndPasswords["jtjadent@gmail.com"]))
print(usernamesAndPasswords["jadent6@byu.edu"])
usernamesAndPasswords["jtjadent@gmail.com"] = "100gh3l30" #assigning new password
print(usernamesAndPasswords["jtjadent@gmail.com"])
print(usernamesAndPasswords)
print(usernamesAndPasswords.values())
print(usernamesAndPasswords.items())


#tuples
tup = (1,"hi",7)
print(tup)

#set
thisIsASet = set()
thisIsASet.add(12)
thisIsASet.add("yolo swag")
print(thisIsASet)
someList = [1,3,2,3,2,2,3,4,2,3,2,1,4,3,7,3,2,1,2,4]
print(someList)
someSet = set(someList)
print(someSet)
print(set("Mississippi"))


hasBoyfriend = False
isBoy = True
boyfriend = None
print("Does he/she have a boyfriend? {}".format(hasBoyfriend))
print("It is {} that boyfriend equals {}.".format(isBoy,boyfriend))
print(type(boyfriend))


#writing to a file
somePreviouslyDefinedText = "Good morning you lovely people."
someMoreText = "\nIt's nice to see y'all."
trialString = str(myDictionary)
print(trialString)

with open("someFileName.txt", "w") as file:
    file.write(somePreviouslyDefinedText)
    file.write("\n"+trialString)

with open("someFileName.txt","a") as file:
    file.write(someMoreText)


    

newString = "This test is on a separate file, wahoo!"
newString2 = "\nAnother python script will attempt to add what's written in here."
with open("sharedFile.txt", "w") as file:
    file.write(newString)
    file.write(newString2)