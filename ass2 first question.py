#First Question
#Base Class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def show(self ):
        print(f" I bought  {self.make} the model is {self.model} which was designed in  {self.year}")
#subclass car
class Car (Vehicle):
    def show(self ):
        print(f"my  {self.make} {self.model} was designed in  {self.year}")
#subclass Bike
class Bike(Vehicle):
    def show(self):
        print(f"my  {self.make} {self.model} was designed in  {self.year}")
#create objects
v1= Vehicle("Honda ", "Fit", 2020)
v1.show()
c1= Car(make="Toyota", model="Corolla", year=2019)
c1.show()
B1=Bike(make="Yamaha", model="R15", year=2021)
B1.show()


#Question 2:Write a function that takes a list of different shapes (such as Circle and Rectangle) and
#calculates the total area of all shapes using polymorphism
