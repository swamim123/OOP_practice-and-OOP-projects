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


harry = Employes("harry",500,12,526.56)
Rohan = Employes("Rohan",600,23,542.25)
karan = Employes.from_dash("karan-400-51-546.54")

Rohan.change_leaves(60)

print(Rohan.no_of_leaves)
print(karan.salary)
karan.printgood("harry")