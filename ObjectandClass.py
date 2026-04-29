#Empty class
# class class1 :
#     pass
'''
class class2 :
    print("welcome to oops content")
    print("="*50)
    print("we will see class and object")

class class3:
    a=10
    b=20
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
obj1=class3()
print(obj1.add())

obj2=class3()
obj2.a=15
print(obj2.a)
print(obj2.b)
ad1=obj2.add()
print(ad1)

obj3=class3()
obj3.b=10
obj3.a=16
ad2=obj3.add()
print(ad2)
'''
# Constructor
class class4:
    def __init__(self):
        print("welcome to Constuctor")
        print("Whenever object is created constructor will run")
        print("="*35)
        print("😎")
obj1=class4()
obj2=class4()


class Employee:
    def __init__(self,name,salary,location):
        self.name=name
        self.salary=salary
        self.location=location
    def welcome_greeting(self):
        return f"welcome to oops concept class {self.name} "
    def grade_calculation(self):
        if self.salary>=100000:
            return "Top grade Employee"
        else:
            return "Second grade Employee"
    def employee_print_details(self):
        return f"Name={self.name},Salary={self.salary},Location={self.location}"
obj1=Employee('Kalai',120000,location='Chennai')
a=obj1.welcome_greeting()
b=obj1.grade_calculation()
c=obj1.employee_print_details()
print(a)
print(b)
print(c)

