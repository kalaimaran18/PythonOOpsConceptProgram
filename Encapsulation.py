#Encapsulation in Python means wrapping data (variables) and methods (functions)
#together inside a class and restricting direct access to some variables.

#Public()
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Arun", 85)
s1.display()
s1.name="Kalai"
s1.display()

#Protected (_)

class Employee:

    def __init__(self):
        self._salary = 50000

class Manager(Employee):

    def show_salary(self):
        print("Salary:", self._salary)
m = Manager()
m.show_salary()
m._salary=45000
m.show_salary()

#Private Class(__)
class BankAccount:

    def __init__(self):
        self.__balance = 10000

    def show_balance(self):
        print("Balance:", self.__balance)
b = BankAccount()
b.show_balance()
b.__balance=100
b.show_balance()

#Exxample
class Car:

    def __init__(self):
        self.__speed = 0

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

c = Car()
c.set_speed(120)
c.__speed=122
print(c.get_speed())
print("Car Speed:", c.get_speed())

#Exxample
class Student:

    def __init__(self):
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value < 0 or value > 100:
            print("Invalid marks")
        else:
            self.__marks = value

s = Student()
s.marks = 85
print("Marks:", s.marks)

# Base class: Encapsulation example
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder   # Public attribute
        self.__balance = balance               # Private attribute

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Deposit method (setter)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited: {amount}")
        else:
            print("❌ Invalid deposit amount")

    # Withdraw method (setter)
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrawn: {amount}")
        else:
            print("❌ Insufficient balance or invalid amount")

    # Protected method — accessible by child classes
    def _update_balance(self, new_balance):
        self.__balance = new_balance


# Derived class: SavingsAccount (inherits BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate  # Public attribute

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"💰 Interest added: {interest}")


# Derived class: CurrentAccount (inherits BankAccount)
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=1000):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    # Override withdraw method
    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            self._update_balance(new_balance)
            print(f"✅ Withdrawn: {amount}")
        else:
            print("❌ Exceeds overdraft limit")


# ----------------------------------------------
# 🧠 Usage Example
# ----------------------------------------------
print("=== Savings Account ===")
savings = SavingsAccount("Alice", 5000)
savings.deposit(1000)
savings.add_interest()
print(f"Final Balance: {savings.get_balance()}\n")

print("=== Current Account ===")
current = CurrentAccount("Bob", 3000, overdraft_limit=2000)
current.withdraw(4000)
print(f"Final Balance: {current.get_balance()}")