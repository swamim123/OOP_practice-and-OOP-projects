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

harry = Employes("harry",500,12,526.56)
Rohan = Employes("Rohan",600,23,542.25)

Rohan.change_leaves(60)
print(Rohan.salary)

print(harry.no_of_leaves)
print(Rohan.no_of_leaves)