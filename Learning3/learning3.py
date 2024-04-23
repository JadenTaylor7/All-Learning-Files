#if else statements
disneyCharacters = {
    "Elsa":"female",
    "Prince Hans":"male",
    "Anna":"female"
}


if disneyCharacters["Elsa"] == disneyCharacters["Anna"]:
    print("Elsa and Anna are the same gender.")
else:
    print("Elsa and Anna are different genders.")

if disneyCharacters["Anna"] == disneyCharacters["Prince Hans"]:
    print("Anna and Prince Hans are the same gender.")
else:
    print("Anna and Prince Hans are different genders.")

#elif statement use
#creating lists
cars = {"Ford","Honda","Hyundai","Chrysler","Toyota","Tesla","Rivian"}
planes = {"B17","B22","Fighter jet","Commercial plane","B27"}
cars.add("Dodge")

    
print(cars.__contains__("Honda"))
print("\n")



if cars.__contains__("Honda") == True:
    print("Honda is a car.")
elif planes.__contains__("Honda") == True:
    print("Honda is a plane")
else:
    print("Vehicle type unknown.")

if cars.__contains__("B17") == True:
    print("B17 is a car.")
elif planes.__contains__("B17") == True:
    print("B17 is a plane")
else:
    print("Vehicle type unknown.")

vehicle1 = "Dodge"

if cars.__contains__(vehicle1) == True:
    print("{} is a car.".format(vehicle1))
elif planes.__contains__(vehicle1) == True:
    print("{} is a plane".format(vehicle1))
else:
    print("Vehicle type unknown.")


#for loop
carsList = list(cars)
carsList.sort()
print(carsList)

for i in carsList:
    print(i)

print("How many cars are in carsList?")
for i in carsList:
    print("IDK")


#practicing or. Checking if specific cars are in the list
for i in carsList:
    if i == "Honda" or i == "Toyota" or i == "Chevrolet":
        print("Found {}".format(i))
    else:
        print("...")

#what numbers are divisible by 3 or 2?
randomNumbers = [3,1,27,300,46,99,256,12,17,3]
misfitNumbers = list()
for i in randomNumbers:
    if i % 3 == 0 and i % 2 == 0:
        print("{} is divisible by 3 and 2.".format(i))
    elif i % 3 == 0:
        print("{} is divisible by 3.".format(i))
    elif i % 2 == 0:
        print("{} is divisible by 2.".format(i))
    else:
        misfitNumbers.append(i)

print("The numbers that aren't divisible by 3 or 2 are: {}".format(misfitNumbers))


#tuple and packing
#Super popular for loop (using tuples in a list)
studentScores = [(90,79,82,76,89),(100,97,90,88,92),(55,0,56,57,0),(98,87,82,85,87),(94,93,76,82,90),(100,94,95,93,98),(88,76,84,82,88),(87,84,92,88,89)]

for student in studentScores:
    print(student)
    

for (a,b,c,d,e) in studentScores:
    print(b) #prints just the first exam scores
    


#dictionary for loop
firstAndLast = {
    "Joe":"Biden",
    "Donald":"Trump",
    "Barak":"Obama",
    "George":"Washington",
    "Thomas":"Jefferson",
    "George W":"Bush"
}

for i in firstAndLast:
    print(i)
for i in firstAndLast.items():
    print(i)
for key,value in firstAndLast.items():
    print(value)


    
#while loop
countDown = 3
while countDown > 0:
    print(countDown)
    countDown = countDown - 1
else:
    print("Blast off!")


foodBars = 12
print("Foodbars start: {}".format(foodBars))
while foodBars >=5:
    foodBars -=3
    print("Food bars left: {}".format(foodBars))
    
else:
    foodBars += 10
    print("Bought some more food bars. We now have: {}".format(foodBars))

#skipping 6
counting = 0
while counting < 10:
    if counting == 6:
        counting += 1
        continue
    print(counting)
    counting += 1


#range
for i in range(0,10,1):
    print(i)
    
    
for i in range(9,-1,-1):
    print(i)


hero = 99
for i in range(0,hero,4):
    print(i)

newHero = [0,3]
newHero.append(6)

for i in range(9,93,3):
    newHero.append(i)


print("Our new hero has values of")
print(newHero)

betterHero = list(range(24,4,-2))
print(betterHero)


#enumerate
#instead of 
indexCount = 0
word = "abcdefghi"
for i in word:
    print(word[indexCount])
    indexCount += 1

#do
for i in enumerate(word):
    print(i)

#or
for i,j in enumerate(word):
    print("At index {}, {}".format(i,j))

for i,j in enumerate(word):
    if i == 3:
        j = j.capitalize()
        print("I see the world in {}{}.".format(i,j))
    else:
        continue


#zip
firstNames = ["Jesus","David","Quentin","Russell","Deiter","Ronald","Jeffrey","Dallin","Henry","Ulysses","Dale","David","D. Todd","M. Russell","Garrett","Gary"]
print(len(firstNames))
lastNames = ["Christ","Bednar","Cook","Nelson","Utchdorf","Rasband","Holland","Oaks","Eyring","Soares","Renlund","Bednar","Chrisoffersen","Ballard","Gong","Stevenson"]
for i in zip(firstNames,lastNames):
    print(i)


#checking if something is in a list
print("a" in firstNames)
print("Jesus" in firstNames)


print(min(firstNames))
print(max(firstNames))
print(min(lastNames))
print(max(lastNames))


#user input
userResult = input("Yo bro, give me a number between 1 and 10: ")
userResult = int(userResult)
if userResult > 10:
    print("Follow the rules please")
elif userResult < 1:
    print("That's too low bro.")
else:
    print("Congrats, you now have {} cows.".format(userResult))


#list comprehension
celsius = [0, 2, 5, 10, 24, 30]
farenheit = [((9/5)*i + 32) for i in celsius ]
print(farenheit)

#vs
faren = []
for i in celsius:
    faren.append((9/5)*i + 32)
print(faren)


#split function
someSentence = "I love to eat flys, said Kermit."
splitSentence = someSentence.split()
print(splitSentence)


zipCodes = {
    84045: "Saratoga Springs",
    84005: "Eagle Mountain",
    84003: "American Fork",
    84097: "Orem",
    84601: "Provo"
}

for key,value in zipCodes.items():
    print(key,value)


with open("happyFile.csv","w") as lolzers:
    for key,value in zipCodes.items():
        lolzers.write("{},{} \n".format(key,value))



readingInDictionary = {}

with open("happyFile.csv","r") as file:
    for i in file:
        x = i.split(",")
        a = x[0] #assigns keys to a
        b = x[1] #assigns values to b
        c = len(b) -2 #removes the \n, and the extra space. -1 might also work
        b = b[0:c] #updates values without \n
        readingInDictionary[a] = b #assigns corresponding values to their keys

print("Let's see if storing in a file to a dictionary works")
print(readingInDictionary)
