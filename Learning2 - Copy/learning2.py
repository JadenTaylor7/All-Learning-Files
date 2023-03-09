#writing to a file
myDictionary = {
    "first":"George Washington",
    "second":"John Adams",
    "third":"Thomas Jefferson",
    "fourth":"James Madison"
}


somePreviouslyDefinedText = "Good morning you lovely people."
someMoreText = "\nIt's nice to see y'all."
trialString = str(myDictionary)
print(trialString)

with open("trialByFile.txt", "w") as file:
    file.write(somePreviouslyDefinedText)
    file.write("\n"+trialString)

with open("trialByFile.txt","a") as file:
    file.write(someMoreText)


#reading from a file
myFile = open("trialByFile.txt")
print(myFile.read())
print(myFile.read()) #won't read again, because cursor has reached the end
myFile.seek(0) #resets the cursor to start at the beginning
print(myFile.read())
myFile.seek(0)

#extrapolating text from a file
extrapolatedTextString = myFile.read()
print("Here is the extrapolated text.\n" + extrapolatedTextString)

myFile.seek(13) #starting at you
fragmentedText1 = myFile.read(8) #only reading 8 indeces
myFile.seek(24) #starting at people
fragmentedText2 = myFile.read(6) #only reading 6 indeces
print(fragmentedText1+ " " + fragmentedText2)


#readlines
myFile.seek(0)
print("\n\n\n")
spicyList = myFile.readlines()
print(spicyList)


#accessing file outside of folder
thefile = open("C:\\Users\\jtjad\\Work\\Learning\\sharedFile.txt")
tempStoring = thefile.read() #store what is already written in the file
addingString = "\nCheck it out bro, I just wrote to this file from a\ntotally different folder!"
with open("C:\\Users\\jtjad\\Work\\Learning\\sharedFile.txt","w") as file:
    file.write(tempStoring) #overwrite file with what's already written
    file.write(addingString) #add new stuff to the file


specialFileMessage = "How did this file appear in this folder?"
specialFileMessage1 = "\nCheck out the FileWriting folder to find out."

with open("C:\\Users\\jtjad\\Work\\Learning\\superSpecialFile.txt","w") as lard:
    lard.write(specialFileMessage + specialFileMessage1)


rickMessage = "Rick may change your life.\n"
rickMessage1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
with open("C:\\Users\\jtjad\\Downloads\\Rick.txt","w") as file:
    file.write(rickMessage + rickMessage1)

print("You should check your downloads file")

with open("trialByFile.txt", "r") as myFile:
    contents = myFile.read()

print("Showing the contents\n" + contents)




print(1 < 2 and 2 < 3)
print(2 == 4 or 3 >= 1)
print(not(2 ==2))