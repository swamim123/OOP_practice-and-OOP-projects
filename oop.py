class Employes():
    not_of_leaves =8

    def __init__(self, ename, esalary, eid, eprice):
        self.name=ename
        self.salary=esalary
        self.id=eid
        self.price=eprice

    def printtable(self):
        return f"the name is {self.name} slary is {self.salary} and id is {self.id} and price {self.price}"

harry = Employes("harry",500,12,526.56)



print(harry.printtable())
print(harry.id)
print(harry.salary)