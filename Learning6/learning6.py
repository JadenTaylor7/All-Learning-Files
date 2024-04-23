import time
#practicing with classes
#object attribute
class MyPythonClass():

    maturity = "Teenager"

    def __init__(self, name, numba = 8018888888): #this initializes "global variables"
        self.name = name
        self.numba = numba



    def printDatInfo(self):
        print("The name is {} and number is {}.".format(self.name, self.numba))


#Johnny is the name, and 4352222222 is the numba 
contact1 = MyPythonClass(name="Johnny", numba=4352222222)

print(contact1.name)
print(contact1.numba)
print(contact1.maturity)


myInfo = MyPythonClass(name="George", numba=9882761454)

print(type(myInfo))
print("\n\nMy name is {n}, and my number is {i}.".format(n = myInfo.name,i = myInfo.numba))
print(myInfo.printDatInfo()) #no need to print this statement, if the method is a print statement too



#practice class methods
class Character():

    def __init__(self, type, age, beans):
        self.type = type #string
        self.age = age #int
        self.beans = beans #boolean

    def stench(self):
        print("Frodo: It stinks in here. I think it's the {}.".format(self.type))

    def attack(self, enemyName = "big fat giant"): #enemyName not a class variable, so the user must pass one.
        print("The {} is in combat with the {}.".format(self.type,enemyName))


gandalf = Character("Wizard", 73, False)
frodo = Character("Hobbit",25,False)
gimly = Character("Dwarf", 57, False)
legolas = Character("Elf", 211, True)
aaragorn = Character("Human", 31, False)


    
if gandalf.beans == True:
    print("Phew, it stinks! Was it the wizard?")
else:
    print("Gandalf: It's a lovely day here in Rivendale.")


gandalf.stench()

legolas.attack("Orcs")
frodo.attack()


print("\n")
#fancy stuff with _init_ method
class HappyRectangle():


    def __init__(self, name, sideA = 2, sideB = 2): #default values if nothing passed in
        self.name = name
        self.sideA = sideA
        self.sideB = sideB
        self.area = sideA * sideB
        self.perimeter = (sideA * 2) + (sideB * 2)

    
    def grandSlam(self, numberOfRectangles): #gets the total area of all the rectangles combined
        totalArea = self.area * numberOfRectangles
        print("The total area of all your rectangles is {} cubits.".format(totalArea))
        if totalArea > 28000 and totalArea < 100000:
            print("                 That's a big boi!           ")
        elif totalArea >= 100000:
            print("        That's the thickest boi of them all! ")
        else:
            pass


    def giveSpecs(self):
        print("The {} is using {} by {} rectangles, making it".format(self.name, self.sideA, self.sideB))
        print("{} cubits per tile.".format(self.area))



lakeHome = HappyRectangle("lake home", 4, 4) #passing in sideA and sideB
standardHouse = HappyRectangle("standard house")
mansion = HappyRectangle("mansion", 8, 12)
wareHouse = HappyRectangle("warehouse", 4,2)


print("The warehouse uses {} by {} rectangles.".format(wareHouse.sideA, wareHouse.sideB))
print("Rectangle area is {} cubits.".format(wareHouse.area))
print("Perimeter is {} cubits.".format(wareHouse.perimeter))
wareHouse.grandSlam(4050)


print("\n")
lakeHome.giveSpecs()
lakeHome.grandSlam(800)

print("\n")
standardHouse.giveSpecs()
lakeHome.grandSlam(1400)

print("\n")
wareHouse.giveSpecs()
wareHouse.grandSlam(4050)

print("\n")
mansion.giveSpecs()
mansion.grandSlam(3015)



print("\n\n")
#class inheritance
#overriding
class Computer():

    def __init__(self, type):
        print("Computer object created") #this should automatically call
        self.type = type

    def printType(self):
        print("Your computer is a {}.".format(self.type))



class Laptop(Computer):

    def __init__(self, type = "Laptop"): #Laptop's init
        Computer.__init__(self, type) #Grabbing Computer's init


    def printType(self): #overriding parent class
        print("I don't wanna do what my parents tell me.")
        print("Not gonna give you the computer type.")
        print("Okay fine, you have a {}.".format(self.type))


mysteryComputer = Computer("...IDK")
hpPavilion = Laptop()
hpPavilion.printType()


print("\n")
#class polymorphism
class Archer():

    def __init__(self, health = 25, range = 3, damage = 5):
        self.health = health
        self.range = range
        self.damage = damage
        self.name = "archer"
        print("Archer Created! Stats:  Health: {}    Range: {}    Damage: {}".format(self.health,range,damage))

    def attack(self):
        print("Archer did {} damage to opponent.".format(self.damage))
        return self.damage

    def hurt(self, impact):
        self.health -= impact
        if impact > 0:
            print("Archer was hit. -{} hp.     Archer health: {}.".format(impact, self.health))
        else:
            pass


class Squire():

    def __init__(self, health = 35, range = 1, damage = 8):
        self.health = health
        self.range = range
        self.damage = damage
        self.name = "squire"
        print("Squire Created! Stats:  Health: {}    Range: {}    Damage: {}".format(self.health,range,damage))

    def attack(self):
        print("Squire did {} damage to opponent.".format(self.damage))
        return self.damage

    def hurt(self, impact):
        self.health -= impact
        if impact > 0:
            print("Squire was hit. -{} hp.     Squire Health: {}.".format(impact, self.health))
        else:
            pass

class Mage():

    def __init__(self, health = 20, range = 3, damage = 6, heal = 4):
        self.health = health
        self.range = range
        self.damage = damage
        self.name = "Mage"
        self.recharging = True
        self.heal = heal
        print("Mage Created! Stats:  Health: {}    Range: {}    Damage: {}   Healing: {}".format(self.health,range,damage,heal))

    def attack(self):
        if self.recharging == True:
            print("Mage did {} damage to opponent.".format(self.damage))
            self.recharging = False
            return self.damage
        else:
            self.health += self.heal
            print("Mage healed {} life.          Mage Health: {}.".format(self.heal, self.health))
            self.recharging = True
            print("Mage did {} damage to opponent.".format(self.damage))
            return self.damage
        

    def hurt(self, impact):
        self.health -= impact
        if impact > 0:
            print("Mage was hit. -{} hp.         Mage Health: {}.".format(impact, self.health))
        else:
            pass


def battle(troop1, troop2, begin = True):
        if begin == True:
            if troop1.range == 1 and troop2.range == 1:
                pass
            elif troop1.range == 1:
                troop1.hurt(troop2.attack())
                troop1.hurt(troop2.attack())
                time.sleep(2)
            elif troop2.range == 1:
                troop2.hurt(troop1.attack())
                troop2.hurt(troop1.attack())
                time.sleep(2)
            else:
                pass
        

        if troop1.health <= 0 and troop2.health <= 0:
            print("Both {} and {} have fallen.".format(troop1.name, troop2.name))
            time.sleep(2)
        elif troop2.health <= 0:
            print("{} has fallen.".format(troop2.name))
            time.sleep(2)
        elif troop1.health <= 0:
            print("{} has fallen.".format(troop1.name))
            time.sleep(2)
        else:
            print("\n")
            troop1.hurt(troop2.attack())
            time.sleep(1.5)
            troop2.hurt(troop1.attack())
            time.sleep(2)
            battle(troop1, troop2, False)

def multiArmyBattle(list1, list2):
    if not list1 and not list2:
        print("Both teams have been defeated.")
        return True
    elif not list1:
        print("Red team defeated. Blue team wins!")
        return True
    elif not list2:
        print("Blue team defeated. Red team wins!")
        return True
    else:
        pass
    
    print("\n\nTeam Red list:") #displays after troop has fallen
    for i in listRed:
        print(i.name, end = ", ")
    print("\n")
    print("\nTeam Blue list")
    for i in listBlue:
        print(i.name, end = ", ")
    print("\n")
    time.sleep(4)
    print("\n")
    battle(list1[0],list2[0])
    if list1[0].health <= 0 and list2[0].health <= 0:
        list1.pop(0)
        list2.pop(0)
        multiArmyBattle(list1, list2)
    elif list1[0].health <= 0:
        list1.pop(0)
        multiArmyBattle(list1, list2)
    elif list2[0].health <= 0:
        list2.pop(0)
        multiArmyBattle(list1, list2)


#test cases
# troopRanged = Archer()
# troopMelee = Squire()

# battle(troopRanged, troopMelee)

# print("\n")
# troopMage = Mage()
# troopRanged2 = Archer()

# battle(troopMage, troopRanged2)

# print("\n")
# troopMage2 = Mage()
# troopMelee2 = Squire()

# battle(troopMage2, troopMelee2)


#test cases 2
# print("\n\n\nOfficial battles begin")
# teamRed1 = Squire()
# teamred2 = Squire()
# teamBlue1 = Archer()
# teamBlue2 = Mage()

# listRed = [teamRed1, teamred2]
# listBlue = [teamBlue1, teamBlue2]

# print("\n       Red Troops")
# for i in listRed:
#     print(i.name)

# print("\n       Blue troops")
# for i in listBlue:
#     print(i.name)

# print("\n")
# multiArmyBattle(listRed, listBlue)



#game setup here
listRed = []
listBlue = []
listRed.clear()
listBlue.clear()
dummyA = Archer()
dummyS = Squire()
dummyM = Mage()
listAvailable = ["A","a","S","s","M","m"]
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def chooseCharacters(size):
    global listRed
    global listBlue
    tempRed = []
    tempBlue = []
    size = int(size)
    print(type(size))
    print("\n\n\n\n\n      Team Red's turn!\n\n")
    for i in range(0,size,1):
        print("Team Red, pick character {}:".format(i+1))
        print("(press A) Archer:  Health: {}    Range: {}    Damage: {}".format(dummyA.health, dummyA.range, dummyA.damage))
        print("(press S) Squire:  Health: {}    Range: {}    Damage: {}".format(dummyS.health, dummyS.range, dummyS.damage))
        print("(press M) Mage:    Health: {}    Range: {}    Damage: {}   Healing: {}".format(dummyM.health, dummyM.range, dummyM.damage, dummyM.heal))
        z = input("(press A, S, or M, then enter)")
        while z not in listAvailable:
            print("\nPlease select a valid input")
            print("Team Red, pick character {}:".format(i+1))
            print("(press A) Archer:  Health: {}    Range: {}    Damage: {}".format(dummyA.health, dummyA.range, dummyA.damage))
            print("(press S) Squire:  Health: {}    Range: {}    Damage: {}".format(dummyS.health, dummyS.range, dummyS.damage))
            print("(press M) Mage:    Health: {}    Range: {}    Damage: {}   Healing: {}".format(dummyM.health, dummyM.range, dummyM.damage, dummyM.heal))
            z = input("(press A, S, or M, then enter)")
        else:
            print("Thank you\n")
            z = z.lower()
            tempRed.append(z)
    print("\n\n\n\n\n      Team Blue's turn!\n\n")
    for i in range(0,size,1):
        print("Team Blue, pick character {}:".format(i+1))
        print("(press A) Archer:  Health: {}    Range: {}    Damage: {}".format(dummyA.health, dummyA.range, dummyA.damage))
        print("(press S) Squire:  Health: {}    Range: {}    Damage: {}".format(dummyS.health, dummyS.range, dummyS.damage))
        print("(press M) Mage:    Health: {}    Range: {}    Damage: {}   Healing: {}".format(dummyM.health, dummyM.range, dummyM.damage, dummyM.heal))
        z = input("(press A, S, or M, then enter)")
        while z not in listAvailable:
            print("\nPlease select a valid input")
            print("Team Blue, pick character {}:".format(i+1))
            print("(press A) Archer:  Health: {}    Range: {}    Damage: {}".format(dummyA.health, dummyA.range, dummyA.damage))
            print("(press S) Squire:  Health: {}    Range: {}    Damage: {}".format(dummyS.health, dummyS.range, dummyS.damage))
            print("(press M) Mage:    Health: {}    Range: {}    Damage: {}   Healing: {}".format(dummyM.health, dummyM.range, dummyM.damage, dummyM.heal))
            z = input("(press A, S, or M, then enter)")
        else:
            print("Thank you\n")
            z = z.lower()
            tempBlue.append(z)
           

    
    for i in tempRed: #building armies
        if i == "a":
            i = Archer() #FIXME should convert from string to class Archer
            troop = Archer()
            listRed.append(troop)
        elif i == "s":
            i = Squire()
            troop = Squire()
            listRed.append(troop)
        elif i == "m":
            i = Mage()
            troop = Mage()
            listRed.append(troop)
        else:
            print("something went wrong. Debug Building armies")
    
    for i in tempBlue: #building armies
        if i == "a":
            i = Archer()
            troop = Archer()
            listBlue.append(troop)
        elif i == "s":
            i = Squire()
            troop = Squire()
            listBlue.append(troop)
        elif i == "m":
            i = Mage()
            troop = Mage()
            listBlue.append(troop)
        else:
            print("something went wrong. Debug Building armies")
        print(i.name)

    print("\nTeams are chosen")
    print("\n")
    print("Game will start in 5")
    time.sleep(1)
    print("Game will start in 4")
    time.sleep(1)
    print("Game will start in 3")
    time.sleep(1)
    print("Game will start in 2")
    time.sleep(1)
    print("Game will start in 1")
    time.sleep(1)


print("Welcome to the battlezone, where two armies battle against each other.")
print("Characters of each army will battle one at a time.")
input("(press enter to continue)")
print("\n\n\n")
battleSize = input("How large should each army be?")
while not battleSize.isdigit():
    print("Invalid response. Must be an integer.")
    battleSize = input("How large should each army be?")
chooseCharacters(battleSize)
multiArmyBattle(listRed, listBlue)


#listBlue.pop(0) #removes first item in list







#practicing abstract class
class Politician():

    def __init__(self, leftCandidate, rightCandidate, party):
        self.leftCandidate = leftCandidate
        self.rightCandidate = rightCandidate
        self.party = party

    def vote(self):
        raise NotImplementedError("Use a subclass bro, not Politician class.")
    
class Democrat(Politician):

    def __init__(self, leftCandidate, rightCandidate, party = "Democrat"):
        Politician.__init__(self, leftCandidate, rightCandidate, party)

    def vote(self):
        return "A " + self.party + " is more likely to vote for " + self.leftCandidate

class Republican(Politician):

    def __init__(self, leftCandidate, rightCandidate, party = "Republican"):
        super().__init__(leftCandidate, rightCandidate, party) #This is the same as declaring Politician._init_

    def vote(self):
        return "A " + self.party + " is more likely to vote for " + self.rightCandidate
    


#naughty = Politician("thing 1", "thing 2", "snickerdoodle" ) #test that parent class sends an error
#print(naughty.vote())
myGuyLandon = Democrat("Joe Biden", "Donald Trump")
print(myGuyLandon.vote())


myGuyDan = Republican("Joe Biden", "Donald Trump")
print(myGuyDan.vote())




#practice with Magic Methods
class Caterpillar():

    def __init__(self, name, color, inches):
        self.name = name
        self.color = color
        self.inches = inches

    def __len__(self):
        return self.inches

    def __str__(self):
        return "{} is a {} caterpillar.".format(self.name, self.color)
    

david = Caterpillar("David", "blue", 3)
print(len(david))
print(david)
david.inches +=3
print(len(david))


#practicing delete (del) attribute
class Satan():

    def __init__(self):
        pass

aDevil = Satan()
print(aDevil) #prints __main__.Satan object at 0x0000022B10FD2B90
del aDevil
#print(aDevil) #NameError: name 'aDevil' is not defined
