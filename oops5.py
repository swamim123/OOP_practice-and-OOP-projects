class Employes():
    no_of_leaves =8

    def __init__(self, ename, esalary, eid, eprice):
        self.name=ename
        self.salary=esalary
        self.id=eid
        self.price=eprice

    def printtable(self):
        return f"the name is {self.name} salary is {self.salary} and id is {self.id}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good "+ string)

#Inheritance
class programmer(Employes):
    no_of_holiday_pakages = 25
    def __init__(self, ename, esalary, eid, eprice, languages):
        self.name = ename
        self.salary = esalary
        self.id = eid
        self.price = eprice
        self.language = languages

    def printprog(self):
        return f"The programmer name is {self.name} salary is {self.salary} and id is {self.id} the languages are {self.language}"

harry = Employes("harry",500,12,526.56)
Rohan = Employes("Rohan",600,23,542.25)

shubham = programmer("shubham",100,11,546.55,["python"])
karan = programmer("karan",200,13,541.54,["python"])

print(karan.printprog())
print(karan.no_of_holiday_pakages)
