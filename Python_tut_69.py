# Setter and Property Decorators

class A:
    def __init__(self, Fname,Lname):
        self.fname=Fname
        self.lname=Lname

    def explain(self):
        return F"This Plyer is {self.fname},{self.lname}"
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@cricket.com"  #Setter
    @email.setter
    def email(self,string):
        print("setting now.....")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

Virat_kohli= A("Virat","Kohli")
Rohit_Sharma=A("Rohit","Sharma")

print(Rohit_Sharma.explain())

print(Virat_kohli.email)
Virat_kohli.fname = "MS"
# Virat_kohli.lname = "Dhoni"
print(Virat_kohli.email)
Virat_kohli.email= "MS.dhoni@gmail.com"
print(Virat_kohli.email)

WC=A("Rishab","pant")
print(WC.email)
