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

class Mother(Grandpa):
    def __init__(self,G_name,G_Age,G_Location,M_name,M_Age,M_Location):
        Grandpa.__init__(self,G_name,G_Age,G_Location)
        self.M_name=M_name
        self.M_Age=M_Age
        self.M_Location=M_Location
    def Mother_print(self):
        print(f"Mother_Name={self.M_name} Age={self.M_Age} Location={self.M_Location}")

class Son(Father,Mother):
    def __init__(self,G_name,G_Age,G_Location,F_name,F_Age,F_Location,M_name,M_Age,M_Location,S_name,S_Age,S_Location):
        Grandpa.__init__(self, G_name, G_Age, G_Location)
        Father.__init__(self,G_name,G_Age,G_Location,F_name,F_Age,F_Location)
        Mother.__init__(self,G_name,G_Age,G_Location,M_name,M_Age,M_Location)
        self.S_name=S_name
        self.S_Age=S_Age
        self.S_Location=S_Location
    def Son_print(self):
        print(f"Son_Name={self.S_name} Age={self.S_Age} Location={self.S_Location}")

s1=Son('Harish',78,'Mumbai','Bharath',45,'Pune','Kani',40,'Delhi','Krishna',17,'Chennai')
s1.Father_print()
s1.Mother_print()
s1.Son_print()