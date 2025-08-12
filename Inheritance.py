#Create a Vehicle class with attributes brand and model. Create a Car class that inherits from Vehicle and adds an attribute num_doors.

# Inheritance problem(1)

class vehicle:
    def brand(self):
        print("This vehicle is audi brand ")
    
    def model(self):
        print("This vehicleis new model")

class car(vehicle):
    def num_doors(self):
        print("The number is AP4529")

c1=car()
c1.brand()
c1.model()
c1.num_doors()


# Define an Animal class with a method sound(). Create a Dog class that inherits from Animal and overrides the sound() method.

#Inheritance problem(2)

class animal:
    def sound(self):
        print("Its able to make sound")
    
class dog(animal):
    def sense(self):
        print("dog have long distance smelling sense")

s1=dog()
s1.sound()
s1.sense()


#Create a Shape class with a method area(). Create a Circle class that inherits from Shape and implements the area() method.

#Inheritance problem(3)

class shape:
    def area(self):
        print("This shape of Square ")

class Circle(shape):
    def value(self):
        print("The area circle is 22/7(r**2)")

d1=Circle()
d1.area()
d1.value()


# Define a Person class with attributes name and age. Create an Employee class that inherits from Person and adds an attribute in department.

# Inheritance problem(4)

class Person: #parent
    def name(self):
        print("He is keerthi")
    
    def age(self):
        print("He is 19")

class Employee(Person):
    def department(self):
        print("He is computer science and engineering")

g1=Employee()
g1.name()
g1.age()
g1.department()



 #Create a Vehicle class with attributes brand and model. Create a Truck class that inherits from Vehicle and adds an attribute capacity.

 # Inheritance problem(5)

class Vehical:
    def brand(self):
        print("Honda")

    def model(self):
        print("Honda shine")

class Truck(Vehical):
    def Capacity(self):
        print("60 km per litre")

f1=Truck()
f1.brand()
f1.model()
f1.Capacity()



      




