#Create a BankAccount class with private attributes balance and account_number. Write methods to deposit and withdraw money.

# Encapsulation (Problem 1)

class BankAccount:
    def public_bank_location(self):                 #Public access
        print("The Bank location: chennai")

        self._type_bank()

    def _type_bank(self):                           #Protect access
        print("The bank type : INDIAN BANK")

        self.__balance()
        

    def __balance(self):                            #Private access
        print("Account balance: 43921")
        print("Account_number: 573981747")

d1=BankAccount()
d1.public_bank_location()


#Define a Person class with private attributes name and age. Write methods to get and set these attributes.

# Encapsulation (Problem 2)

class Person:
    def details(self):                  #Public access
        print("The person is Rich")

        self._his_profession()

    def _his_profession(self):          #Protect access
        print("He is a doctor")
      
        self.__his_name_age()

    def __his_name_age(self):           #Private access
    
        print("His name is Raju")
        print("He is 53 age old")

s1=Person()
s1.details()

#Create a Student class with private attributes name, roll_number, and grade. Write methods to get and set these attributes.

# Encapsulation (Problem 3)

class Student:
    def Study(self):                        #Public access
        print("He is good in Study")

        self._mark()

    def _mark(self):                        #Protect access
        print("He scored more than 80")

        self.__name_roll_number_grade()
       

    def __name_roll_number_grade(self):     #Private access
        print("He is name: rrrrr")
        print("He is roll_number: 345")
        print("Grade:A+")

a1=Student()
a1.Study()

# Define a Car class with private attributes brand, model, and year. Write methods to get and set these attributes.

# Encapsulation (Problem 4)

class car:

    def car_detail(self):          #Public access
        print("Its Expensive")

        self.__brand()
        self.__model()
        self.__year()

    def __brand(self):              #Private access
        print("Audi")
    def __model(self):
        print("45 T")

    def __year(self):
        print("2020")

x1=car()
x1.car_detail()