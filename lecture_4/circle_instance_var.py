import math

class Circle:
    def __init__(self,name,radius,PI):
        self.name=name
        self.radius=radius
        self.PI=PI

    def area(self):
        return self.PI*self.radius**2

    def __del__(self):
        print("This process is End!")

    
c1= Circle('C1',4,math.pi)
print('c1의 면적=',c1.area())
print(c1.__dict__)