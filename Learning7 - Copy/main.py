from someModule import printSomethingCool
from secondModule import investCash
from thirdModule import accessGranted

printSomethingCool() #accessing from someModule
print("\n")
investCash() #accessing from secondModule

response = input("Would you like to continue? (Y for yes, N for no)")
yesResponses = ["Y","y","yes","Yes","YES"]
if (response in yesResponses):
    accessGranted() #accessing from thirdModule
else:
    ("Okay, thanks for trying out the code!")
