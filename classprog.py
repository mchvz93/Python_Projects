import math

class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    #methods
    def getArea(self):
        return self.radius*self.radius*math.pi
    def getPerimeter(self):
        return 2*self.radius*math.pi
    def setRadius(self, radius):
        self.radius = radius

def main():
    #create a cirle object with radius = 1
    circle1 = Circle()
    print("the area of the circle of the radius ", circle1.radius, "is", circle1.getArea())

    circle2 = Circle(25)
    print("the area of the circle of the radius ", circle2.radius, "is", circle2.getArea())
	
#modify circle radius
    circle2.radius =100 #direct access 
    print("the area of the circle of the radius ", circle2.radius, "is", circle2.getArea())

main()
	
'''Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
the area of the circle of the radius  1 is 3.141592653589793
the area of the circle of the radius  25 is 1963.4954084936207
the area of the circle of the radius  100 is 31415.926535897932
>>> '''
