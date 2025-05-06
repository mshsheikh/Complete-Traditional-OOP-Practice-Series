from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == "__main__":
    rect = Rectangle(4, 5)
    print("Area of Rectangle:", rect.area())