#Object Oriented Programming
#Homework Assignment
import math
import cmath


#Problem 1
#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.x1 = coor1[0]
        self.x2 = coor2[0]
        self.y1 = coor1[1]
        self.y2 = coor2[1]
    
    def distance(self): 
        #print("Coordinate1 x = {}, y = {}".format(self.coor1[0],self.coor1[1])) #for testing
        #print("Coordinate2 x = {}, y = {}".format(self.coor2[0],self.coor2[1])) #for testing
        solveX = (self.x2 - self.x1)**2
        solveY = (self.y2 - self.y1)**2
        #print("SolveCoor1 is {} and SolveCoor2 is {}".format(solveX, solveY)) #for testing
        datDistance = math.sqrt(solveX + solveY)
        print("The distance is {}".format(datDistance))
        return datDistance
    
    def slope(self):
        yDistance = self.y2 - self.y1
        #print(yDistance)
        xDistance = self.x2 - self.x1
        #print(xDistance)
        datSlope = yDistance/(xDistance + 0.00)
        print("Slope is {} or {}/{}".format(datSlope, yDistance, xDistance))
        return datSlope
        
# EXAMPLE OUTPUT
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance() #Should print 9.433981132056603
li.slope() #Should print 1.6






print("\n")
#Problem 2
#Fill in the class

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.einstein = radius
        
    def volume(self): #pi r squared times h
        datVolume = cmath.pi * (self.einstein**2) * self.height
        print("Cylinder volume is {:1.2f}".format(datVolume))
        return datVolume
    
    def surface_area(self): #2 * pi * r * (r+h)
        rPlusH = self.einstein + self.height
        datSurface = 2 * cmath.pi * self.einstein * rPlusH
        print("Cylinder surface area is {:1.1f}".format(datSurface))
        return datSurface

# EXAMPLE OUTPUT
c = Cylinder(2,3)
c.volume() #Should print 56.52
c.surface_area() #Should print 94.2




#practice with math vs cmath
#print(math.sqrt(9))
#print(cmath.sqrt(9))