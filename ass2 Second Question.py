#POLYMOPHISM
class Shape :
    def area(self  ):
        return self.area
#first subclass shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
       return self.radius * self.radius * 3.14 **2
#second subclass shape
class Rectangle (Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
#Third subclass shape
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height / 2
#

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
#List
Shape =[Circle(5), Rectangle(5, 5), Triangle(5, 5), Square(3)]
for shape in Shape :
    print(shape.area())
