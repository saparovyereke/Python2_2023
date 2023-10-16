import math
class Point:
    def __init__(self, xCoord=0, yCoord=0):
        self.__xCoord = xCoord
        self.__yCoord = yCoord
       
    # get x coordinate
    def get_xCoord(self):
        return self.__xCoord
   
    # get y coordinate
    def get_yCoord(self):
        return self.__yCoord
   
    # set x coordinate
    def set_xCoord(self, xCoord):
        self.__xCoord = xCoord
       
    # set y coordinate
    def set_yCoord(self, yCoord):
        self.__yCoord = yCoord
       
    # get current position
    def get_position(self):
        return self.__xCoord, self.__yCoord
   
    # change x & y coordinates by p & q
    def move(self, p, q):
        self.__xCoord += p
        self.__yCoord += q
       
    # overload + operator
    def __add__(self, point_ov):
        return Point(self.__xCoord + point_ov.__xCoord, self.__yCoord + point_ov.__yCoord)
   
    # overload > (greater than) operator
    def __gt__(self, point_ov):
        return math.sqrt(self.__xCoord ** 2 + self.__yCoord ** 2) > math.sqrt(point_ov.__xCoord ** 2 + point_ov.__yCoord ** 2)
    
    # overload - operator
    def __sub__(self, point_ov):
        return Point(self.__xCoord - point_ov.__xCoord, self.__yCoord - point_ov.__yCoord)
    #print
    def __str__(self):
        return str(f'The x coordinate is {self.__xCoord} and the y coordinate is {self.__yCoord}')      
    
point1 = Point(1, 2)
# point2 = Point(map(int, input().split()))
point2 = Point(2, 3)
point3 = point1 - point2
print(point3)
