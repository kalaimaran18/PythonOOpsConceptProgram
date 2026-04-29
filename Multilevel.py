class Grandpa:
    def __init__(self,G_name,G_Age,G_Location):
        self.G_name=G_name
        self.G_Age=G_Age
        self.G_Location=G_Location
    def Grandpa_Print(self):
        print(f"Grandpa_name={self.G_name} Age={self.G_Age} Location={self.G_Location}")

class Father(Grandpa):
    def __init__(self,G_name,G_Age,G_Location,F_name,F_Age,F_Location):
        Grandpa.__init__(self,G_name,G_Age,G_Location)
        self.F_name=F_name
        self.F_Age=F_Age
        self.F_Location=F_Location
    def Father_print(self):
        print(f"Father_name={self.F_name} Location={self.F_Location} Age={self.F_Age}")

class Son(Father):
    def __init__(self,G_name,G_Age,G_Location,F_name,F_Age,F_Location,S_name,S_Age,S_Location):
        Father.__init__(self,G_name,G_Age,G_Location,F_name,F_Age,F_Location)
        self.S_name=S_name
        self.S_Age=S_Age
        self.S_Location=S_Location
    def Son_print(self):
            print(f"Son_name={self.S_name} Age={self.S_Age} Location={self.S_Location}")
S=Son('Ramesh',70,'Theni','Kalai',45,'Bodi','Sai',11,'Chennai')
S.Grandpa_Print()
S.Father_print()
S.Son_print()
