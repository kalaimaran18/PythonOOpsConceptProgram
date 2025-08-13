#Define a Person class with a constructor that takes name and age as arguments. Create an object and print its attributes.

# Constructors (Problem 1)

class Person:
    def __init__(self,name,age):
        self.x=name
        self.y=age
    
    def display(self):
        print(f"name:{self.x},age:{self.y}")

s1=Person(name='kalai', age='20')
s1.display()
        
#Create a Car class with a constructor that takes brand, model, and year as arguments. Write a method to display the car's details.

# Consructors (Problem 2)

class Car:
    def __init__(self,brand,model):
        self.t=brand
        self.j=model

    def display(self):
         print(f"brand:{self.t}:,model:{self.j}")
    
r1=Car(brand='Honda' , model='Shine')
r1.display()

# Define a Student class with a constructor that takes name, roll_number, and grade as arguments. Create an object and print its attributes.

#Consructors (Problem 3)

class Student:
    def __init__(self,name,roll_number):
        self.y=name
        self.r=roll_number

    def display(self):
        print(f"name:{self.y}, roll_number:{self.r}")

a1=Student(name='KKKKK' , roll_number='24')
a1.display()


 #Create a Rectangle class with a constructor that takes length and width as arguments. Write methods to calculate the area and perimeter.

# Constructors (Problem 4)

class Rectangle:
    def __init__(self,lenght,width):
        self.v=lenght
        self.m=width

    def display(self):
        print(f"lenght:{self.v}, width:{self.m}")

z1=Rectangle(lenght='45 cm' , width='32 cm')
z1.display()        