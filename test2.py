class Circle:
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        self.Area= 3.14*self.radius**2
        print(self.Area)
    def Perimeter(self):
        return 2*(22/7)*self.radius
Circle(21).Area()

print(Circle(21).Perimeter())
    