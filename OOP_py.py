# Question 1
#Polymorphism

class Shape():
    def Area(self):
        return 0
 
class Rectangle():
    def Area(self):
        l=10
        b=5
        print(l*b)
s1=Rectangle()
s1.Area()


# Question 2
 
class Person():
    def __init__(self,name):
        self.name=name
        
class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
       
        self.grade=grade
      
    def display(self):
        print(self.name,self.grade)

t1=Student("Kalai","A")
t1.display()
       