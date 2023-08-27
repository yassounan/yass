from math import pi 
 
#Function calculates area and circumference of a circle 
#r is the radius 
 
def calc_area_circm(r): 
    return pi * r * r, 2 * pi * r 
 
 
# Driver code 
 
area, circm = calc_area_circm(10) 
print('Area=',area) 
print('Circumference=',circm)