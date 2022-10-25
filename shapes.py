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
        self.points = []
        for arg in args:
            self.points.append(arg)

    def __str__(self):
        return f"Curve with points: {self.points}"

    def __repr__(self):
        return self.points

    def append_if_valid(self,curvePoint):
        if curvePoint not in self.points:
            self.points.append(curvePoint)
        else:
            print("Point already in curve")

    def __getitem__(self, index):
        return self.points[index]

    def __setitem__(self, index, item):
        self.points[index] = item

# define a curve
cur = Curve(Point(1,1),Point(2,4),Point(3,9))
# cur = Curve(Point(1,1),(2,2)) # should raise a TypeError
print(cur)
print(cur.__repr__())
# return a point/item
print(cur[1]) # == print(cur.__getitem__(1))
# return points/items i.e. subcurve
print(cur[0:2]) # == print(cur.__getitem__(0:2))
# update point
cur[1] = Point(1,1) # == print(cur.__setitem__(1,Point(1,1)))
# cur[1] = (1,1) # should raise a TypeError
print(cur)
