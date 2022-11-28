class circle:
    def __init__(self, r):
        self.r = r
    def radius(self):
        return self.r
    def diameter(self):
        return self.r*2
    def __len__(self):
        return 2 * 3.14 * self.r
    def area(self):
        return 3.14 * self.r**2
    def newrad(self):
        return self.r * n
    def __mul__(self, other):
        return circle((2 * 3.14 * self.r)*(2 * 3.14 * self.r * other.r))
r = int(input())
n = int(input())
c = circle(r)*circle(n)
a = circle(r)
print(a.radius(),a.diameter(),a.__len__(),a.area(),a.newrad(),c.r, sep='\n')


class cir(circle):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def center(self):
        return self.x, self.y
    def moving(self):
        x=self.x + X
        y=self.y + Y
        return x, y
    def distance(self):
        return ((self.x + X)**2 + (self.y + Y)**2)**0.5
x, y = map(int, input().split())
X, Y = map(int, input().split())
a=cir(x, y)
print(a.center(),a.moving(),a.distance(), sep='\n')
