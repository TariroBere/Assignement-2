class Shape:
    def __init__(self  ):
        print("Shape Initialized")
    def calculate_area(self):
        pass # base method does nothing
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()#demonstration of calling shape's constructor again
        self.width = width
        self.height = height
    def calculate_area(self):
        super(). __init__()
        return  self.width * self.height
Rectangle=Rectangle(10,20)
area=Rectangle.calculate_area()
print(area)