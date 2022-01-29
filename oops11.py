from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0                           #abstract Base class and Abstract Method

class Rectangle(Shape):
    type= "Recrabgle"
    side=4
    def __init__(self):
        self.length=4
        self.breadth=6



    def printarea(self):
        return self.length * self.breadth

rect = Rectangle()
print(rect.printarea())