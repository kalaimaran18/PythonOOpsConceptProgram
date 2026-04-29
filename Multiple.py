class Father:
    def __init__(self,fname,fage,flocation):
        self.fname = fname
        self.fage = fage
        self.flocation = flocation
    def Father_print(self):
        print(f"Father name = {self.fname},Location = {self.flocation},Age = {self.fage}")

class Mother:
    def __init__(self,M_name,M_age,M_location):
        self.M_name = M_name
        self.M_age = M_age
        self.M_location = M_location
    def Mother_print(self):
        print(f"Mother name = {self.M_name},Location = {self.M_location},Age = {self.M_age}")

class Son(Father,Mother):
    def __init__(self,fname,fage,flocation,M_name,M_age,M_location,S_name,S_age,S_location):
        Father.__init__(self,fname,fage,flocation)
        Mother.__init__(self,M_name,M_age,M_location)
        self.name = S_name
        self.age = S_age
        self.location = S_location
    def Son_Print(self):
        print(f"Son name = {self.name},Age = {self.age},Location = {self.location}")
S=Son('Elango',60,'Selam','Abi',54,'Ariyalur','Vishnu',23,'Chennai')
S.Father_print()
S.Mother_print()
S.Son_Print()

