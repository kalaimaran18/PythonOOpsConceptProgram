class father:
    def __init__(self,name,Age,Location):
        self.name=name
        self.Age=Age
        self.Location=Location
    def Father_print(self):
        print(f"Father name = {self.name},Location = {self.Location},Age = {self.Age}")

class Son(father):
    def __init__(self,name,Age,Location,S_name,S_Age,S_Location):
        father.__init__(self,name,Age,Location)
        self.S_name=S_name
        self.S_Age=S_Age
        self.S_Location=S_Location
    def Son_print(self):
        print(f"Son name = {self.S_name},Age = {self.S_Age},Location = {self.S_Location}")

S=Son('Vasanth',39,'Madhurai','Saran',12,'Chennai')
S.Father_print()
S.Son_print()
