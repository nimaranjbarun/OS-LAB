import math
import random

class Shape:
    def __init__(self,perimeter=0,area=0):
        self.perimeter = perimeter
        self.area = area
        
    def get_perimeter(self): 
        print("Perimeter : "+str(self.perimeter))
        
    def get_area(self): 
        print("Area : "+str(self.area)) 
        
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(self.calc_perimeter(),self.calc_area())

    def calc_area(self):
        return (self.radius**2)*math.pi
        
    def calc_perimeter(self):
        return (self.radius*2)*math.pi
         
class Rectangle(Shape):
    def __init__(self,width,height):
         self.width = width
         self.height = height
         super().__init__(self.calc_perimeter(),self.calc_area())
         
    def calc_area(self):
        return self.width * self.height
        
    def calc_perimeter(self):
        return (self.width + self.height)*2
        
print("******************* Rectangle *******************\n")
rectangle=Rectangle(random.randint(1,10),random.randint(1,10))
rectangle.get_perimeter()
rectangle.get_area()
print("\n******************* Circle *******************\n")
circle=Circle(random.randint(1,10))
circle.get_perimeter()
circle.get_area()    
      

        