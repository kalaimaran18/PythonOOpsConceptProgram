#Constructors using Inheritance

class Employee():
    def __init__(self):              
        print("Kalai")
        print(31)
        super().__init__()
    
    
class Manager(Employee):
    def __init__(self):
       print("CSE")
       super().__init__()

    def display(self):
        print(self.name,self.salary,self.department)

ob1=Manager()

