#Operator Overloding and Dunder Method
class Employee:
    no_of_leaves=8
    def __init__(self,Nmae,Salary,Role):
        self.name=Nmae
        self.salary=Salary
        self.role=Role

    def printdetails(self):
        return f"The name is {self.name} and salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves=newleaves

    def __mul__(self, other):              # Operator Overloading
        return self.salary*other.salary    #search on google Mapping operators to Function

    def __repr__(self):
        return f"Employe ('{self.name}'{self.salary},'{self.role}')"

    def __str__(self):
        return f"Employe name is {self.name} and salary is {self.salary} reole is {self.role}"

emp1=Employee("Harry",10,"programmer")
emp2=Employee("Rohan",5,"cleanner")

print(str(emp1))
print(repr(emp2))