class Animal():
    def sound(self):
        print("Animal makes a Sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Bird(Animal):
    def sound(self):
        print("Birds are Singing")
    
d1=Dog()
d1.sound()

b1=Bird()
b1.sound()