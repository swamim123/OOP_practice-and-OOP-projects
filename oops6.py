class Employes():
    no_of_leaves =8
    var=8

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

class player:
    no_of_games = 4
    var=9
    def __init__(self,ename, egame):
        self.name= ename
        self.game= egame

    def printdetails(self):
        return f"The name is {self.name} and game  is {self.game}"
#Multipal Inheritance

class coolprogrammer(Employes,player):

    pass


harry = Employes("harry",500,12,526.56)
Rohan = Employes("Rohan",600,23,542.25)

shubham = player("shubham",["cricket"])
karan = coolprogrammer("karan",900,20,254.26)
det=karan.printtable()
print(det)
print(karan.var)


