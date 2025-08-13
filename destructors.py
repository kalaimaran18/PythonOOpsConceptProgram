#Define a Person class with a destructor that prints a message when an object is destroyed.

# Destructors (Problem 1)

class Person:
    def __init__(self, name):
        self.name=name
        print("My name is",name)

    def __del__(self):                          #destructor key word is __del__
        print("The object is destroyed")

w1=Person(name='kalai')
del w1 

#Create a Book class with a destructor that prints a message when an object is destroyed.

# Desturctors (Problem 2)

class book:
    

    def __init__(self,name,author):
        self.author=author
        self.name=name

        print("The book name is",name )
        print("The author name is",author)

    def __del__ (self):
        print("The object is destroyed")
   

s1=book(name='WINGS OF FIRE' , author='APJ Abdul kalam')
del s1
