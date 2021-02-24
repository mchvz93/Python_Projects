import math
class Circle:

    def __init__(self, radius = 1):
        self.__radius = radius
    def getArea(self):
        return self.__radius*self.__radius*math.pi
    def getPerimeter(self):
        return 2*self.__radius*math.pi
    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius
		
def main():

    Circle2.setRadius(5)
    print("the area of the circle of the radius ", Circle2.getRadius(), "is", Circle2.getArea())

main()
