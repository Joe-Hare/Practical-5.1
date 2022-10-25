class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point on the graph is at (x={self.x}, y={self.y})"

    def __repr__(self):
        return f"({self.x},{self.y})"


class Rectangle():
    def __init__(self, o, w, l):
        self.o = o
        self.w = w
        self.l = l

    def __str__(self):
        return f"Rectangle of width {self.w} and length {self.l}, with its centre at point ({self.o.x},{self.o.y})"

    def __repr__(self):
        return f"{self.w},{self.l},{self.o.__repr__()}"

    def area(self):
        return self.w * self.l

    def perimeter(self):
        return (2*self.w)+(2*self.l)

    def __contains__(self, p):
        if p.x >= self.o.x-(self.w/2) and p.x <= self.o.x+(self.w/2) and p.y >= self.o.y - (self.l / 2) and p.y <= self.o.y + (self.l / 2):
            return True
        else:
            return False

class Circle():
    def __init__(self, o, r):
        self.o = o
        self.r = r

    def __str__(self):
        return f"Circle of radius {self.r} and centre point ({self.o.x},{self.o.y})"

    def __repr__(self):
        return f"{self.r},{self.o.__repr__()}"

    def area(self):
        return 3.1415*(self.r**2)

    def perimeter(self):
        return 3.1415*self.r*2

    def __contains__(self, p):
        if (((self.o.x-p.x)**2)+((self.o.y-p.y)**2))**0.5 <= self.r:
            return True
        else:
            return False

class Curve():
    def __init__(self,*args):
        #https: // www.geeksforgeeks.org / args - kwargs - python /
        pass

print("hi")
