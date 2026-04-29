class Father:
    def __init__(self,Fname,F_Age,F_Location):
       self.Fname=Fname
       self.F_Age=F_Age
       self.F_Location=F_Location
    def Father_print(self):
        print(f"Father name = {self.Fname},Age = {self.F_Age},Location = {self.F_Location}")

class Son1(Father):
    def __init__(self,Fname,F_Age,F_Location,S1_name,S1_Age,S1_Location):
        Father.__init__(self, Fname, F_Age, F_Location)
        self.S1_name=S1_name
        self.S1_Age=S1_Age
        self.S1_Location=S1_Location
    def Son1_print(self):
        print(f"Son1_name={self.S1_name},Age={self.S1_Age},Location={self.S1_Location}")


class Son2(Father):
    def __init__(self, Fname, F_Age, F_Location, S2_name, S2_Age, S2_Location):
        Father.__init__(self, Fname, F_Age, F_Location)
        self.S2_name = S2_name
        self.S2_Age = S2_Age
        self.S2_Location = S2_Location
    def Son2_print(self):
        print(f"Son2_name={self.S2_name},Age={self.S2_Age},Location={self.S2_Location}")

class Son3(Father):
    def __init__(self, Fname, F_Age, F_Location, S3_name, S3_Age, S3_Location):
        Father.__init__(self, Fname, F_Age, F_Location)
        self.S3_name = S3_name
        self.S3_Age = S3_Age
        self.S3_Location = S3_Location
    def Son3_print(self):
        print(f"Son3_name={self.S3_name},Age={self.S3_Age},Location={self.S3_Location}")

S1=Son1('Suresh',78,'Thambaram','Krish',35,'Mudichur',)
S1.Father_print()
S1.Son1_print()

S2=Son2('Suresh',78,'Thambaram','Vishnu',22,'Pallavaram')
S2.Father_print()
S2.Son2_print()

S3=Son3('Suresh',78,'Thambaram','Kalai',21,'Chrompet')
S3.Father_print()
S3.Son3_print()



