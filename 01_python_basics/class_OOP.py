
# Create a class named 'Cylinder' which takes in height and radius and 
# has the following methods: volume of the cylinder, surface area of the cylinder

class Cylinder():
    import math
    
    
    def __init__(self,height=1,radius=1):
        
        self.height = height
        self.radius = radius
        
    
    
    def volume(self):
        ''' volume = pi.r^2.h'''
        vol = (self.math.pi)*(self.radius**2)*(self.height)
        return f" volume of cylinder: {vol} "
    
    def surface_area(self):
        '''surface area = 2*pi*r*h + 2*pi*r^2'''
        sa = (2*(self.math.pi)*(self.radius)*(self.height)) + (2*(self.math.pi)*(self.radius)**2)
        return f" surface area of cylinder: {sa} "
    

c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())




# create a class named Line which takes in coordinates in the form of tuples and
# has the following methods: distance between coordinates, slope of line formed 

class Line():
    import math
    
    def __init__(self,coor1,coor2):
        self.coor1 =coor1
        self.coor2 =coor2
        
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        dis = Line.math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return f"distance between coordinates: {dis} "
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        slop = (y2-y1)/(x2-x1)
        return f"slope of the line formed: {slop}"
    

li = Line((3,2),(8,10))

print(li.distance())
print(li.slope())
        
            