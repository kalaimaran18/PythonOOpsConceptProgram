# Single Inheritance

class ramesh():
    def land(self):
        print("dad's land")

class kalai(ramesh):
    def laptop(self):
        print("Kalai laptop")

K=kalai()
K.land()
K.laptop()


# Multiple Inheritance
class ramesh():
    def land(self):
        print("dad's land")

class kalai():
    def laptop(self):
        print("Kalai laptop")

class Gowtham(ramesh,kalai):
    def Bike(self):
        print("Gowtham Bike")

Gow=Gowtham()
Gow.Bike()
Gow.land()
Gow.laptop()