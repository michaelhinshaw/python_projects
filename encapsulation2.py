import abc

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, x,y):
        self.l = x
        self.b = y
    def area(self):
        return self.l*self.b
r = Rectangle(20, 40)
print ('area: ',r.area())
