#GEOMETRIC CLASSES

''' This document is all about creation of geometric classes '''

import math


# Create a class named 'Cylinder' which takes in height and radius and
# has the following methods: volume of the cylinder, surface area of the cylinder

class Cylinder():
    ''' This class takes in radius and height and
    can be used to obtain volume and surface area of the cylinder'''

    def __init__(self,height=1,radius=1):

        self.height = height
        self.radius = radius



    def volume(self):
        ''' volume = pi.r^2.h'''

        vol = (math.pi)*(self.radius**2)*(self.height)
        return f" volume of cylinder: {vol} "

    def surface_area(self):
        '''surface area = 2*pi*r*h + 2*pi*r^2'''

        sa_top_bottom = (math.pi)*(self.radius)**2
        sur_area = (2*(math.pi)*(self.radius)*(self.height)) + (2*sa_top_bottom)
        return f" surface area of cylinder: {sur_area} "






# create a class named Line which takes in coordinates in the form of tuples and
# has the following methods: distance between coordinates, slope of line formed


class Line():

    ''' This class takes in coordinates of two points and
    can be used to obtain the distance between points and slope of the line formed'''



    def __init__(self,coor1,coor2):
        self.coor1 =coor1
        self.coor2 =coor2


    def distance(self):
        '''distance is given by: sqrt((x2-x1)^2 |+ (y2-y1)^2))'''
        x_1,y_1 = self.coor1
        x_2,y_2 = self.coor2

        dis = math.sqrt((x_2-x_1)**2 + (y_2-y_1)**2)
        return f"distance between coordinates: {dis} "

    def slope(self):
        '''slope is given by:  (y2-y1)/(x2-x1)'''
        x_1,y_1 = self.coor1
        x_2,y_2 = self.coor2

        slop = (y_2-y_1)/(x_2-x_1)
        return f"slope of the line formed: {slop}"







#create a class named 'Cone' which takes in radius and height as aguments and
# has the following methods: volume of a cone, surface area of the cone

class Cone():

    ''' This class takes in radius and height and
    can be used to obtain volume and surface area of the cone'''



    def __init__(self, radius, height):
        self.radius = radius
        self.height = height


    def volume(self):
        ''' Volume of the cone is given by:
            pi*(r^2)*(h/3) '''

        vol = (math.pi)*(self.radius**2)*(self.height/3)
        return f"volume of cone: {vol}"

    def surface_area(self):
        ''' Surface area of cone is given by:
        pi*r*(r + sqrt(h^2 + r^2))

        part_1 = pi*r
        part_2 = (r + sqrt(h^2 + r^2))'''

        part_1 = (math.pi*self.radius)
        part_2 = (self.radius + (math.sqrt(self.height**2 + self.radius**2)))
        sur_area = part_1*part_2
        return f'surface area of cone: {sur_area}'




if __name__ == '__main__':

    c = Cylinder(2,3)

    print(c.volume())
    print(c.surface_area())



    li = Line((3,2),(8,10))
    print(li.distance())
    print(li.slope())


    cone = Cone(radius=1, height=3)

    print(cone.volume())
    print(cone.surface_area())
