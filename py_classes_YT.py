#classes necessary for:
#safe from bugs
#easy to understand
#ready for change

import turtle

class Polygon:
    def __init__(self, sides, name, size=100, color="black", line_thickness=2):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides

    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180-self.angle)
        #turtle.done()

##Subclasses##########################################################        

class Square(Polygon):
    def __init__(self, size=100, color="black", line_thickness=2):
        super().__init__(4, "SWA", size, color, line_thickness)

    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()
        

square = Square(color= "#123abc")

print(square.sides)
print(square.angle)
print(square.draw())

turtle.done()

################# Using the Code in general ################################

##square = Polygon(4, "Square")
##pentagon = Polygon(5, "Pentagon")
##
##print("class name: ", square.name)
##print("number of sides: ", square.sides)
##
##print("class name: ", pentagon.name)
##print("number of sides: ", pentagon.sides)
##
##print("==================================")
##print(square.interior_angles)
##print(square.angle)
##
##
##hexagon = Polygon(6, "Hexagon", color="blue")
##hexagon.draw()
############### Using the Code in general - Done ##########################

