class A:
    def met(self):
        print("this is a method from class A")      #Multipal inheritance

class B(A):
    def met(self):
        print("this is a method from class B")
class C(A):
    def met(self):
        print("this is a method from class C")

class D(C,B):

    pass
a=A()
b=B()
c=C()
d=D()

c.met()