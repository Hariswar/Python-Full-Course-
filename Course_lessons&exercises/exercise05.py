#This code will find the area of a circle 
import math

radius = float(input(f'Enter the radius of a circle: '))
area = math.pi * pow(radius,2)  # pi * r^2
print(f'The area of the circle is: {round(area,2)}cm^2') # rounds the area by 2 decimal point. 