# Statements Assessment Test
# Let's test your knowledge!

# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'

for i in st.split():
    if i[0].lower() == "s": #doesn't care about casing
        print(i)


# Use range() to print all the even numbers from 0 to 10.
for i in range(0,11,2):
    print(i)


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
happyList = [i for i in range(1,51,3)]
print(happyList)
#I personally feel it's easier to read doing the following:
newHappyList = []
for i in range(1,51,3):
    newHappyList.append(i)
print(newHappyList)



# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for i in st.split():
    if len(i)%2 == 0:
        print(i)



# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" 
# instead of the number, and for the multiples of five print "Buzz". For numbers which are 
# multiples of both three and five print "FizzBuzz".

themIntegers = []
for i in range(1,101,1):
    if (i%3 == 0) and (i%5 == 0):
        themIntegers.append("FizzBuzz")
    elif i%3 == 0:
        themIntegers.append("Fizz")
    elif i%5 == 0:
        themIntegers.append("Buzz")
    else:
        themIntegers.append(i)

print(themIntegers)
#if you want to print what's in the list separately
# for i in themIntegers:
#     print(i)


#If you don't want it in a list, and are just printing them
# for i in range(1,100,1):
#     if (i%3 == 0) and (i%5 == 0):
#         print("FizzBuzz")
#     elif i%3 == 0:
#         print("Fizz")
#     elif i%5 == 0:
#         print("Buzz")
#     else:
#         print(i)




print("\n")
# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

#I personally like this way better
#print(st[0:3]) #test case
savedList = []
for i in st.split():
    firstThree = i[0:3]
    savedList.append(firstThree)
    
print(savedList)

#comprehended way
comprehendedList = [i[0:3] for i in st.split()]
print(comprehendedList)

#finished. Yay!