import time
class A:
    def __init__(self, fname,lname):
        self.fname=fname
        self.lname=lname

    def explain(self):
        return f"This player is {self.fname},{self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return f"Email is not set"
        return f"{self.fname}.{self.lname}@cricket.com"  #Setter
    @email.setter
    def email(self, string):
        print("setting now.....")
        time.sleep(2)
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fanme=None
        self.lname=None

Virat_kohli= A("Virat","Kohli")
# Rohit_Sharma=A("Rohit","Sharma")

print(Virat_kohli.email)
Virat_kohli.fname = "MS_Dhoni"
print(Virat_kohli.email)
Virat_kohli.email= "MS.dhoni@gmail.com"
print(Virat_kohli.fname)

del Virat_kohli.email
print(Virat_kohli.email)

Virat_kohli.email = "Shikar.Dhawan@gmail.com"
print(Virat_kohli.email)

#Object introspection
Scoopan=A("\nscoopan","python")
print(Scoopan.email)

print(dir(Scoopan))