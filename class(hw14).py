#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:33:20 2021

建立類別並從父類別繼承
"""

class Polygon():
    def __init__(self, num_sides , perimeter = None ):        
        self.num_sides = num_sides
        self.perimeter = perimeter
        """
        A class to capture information about side length, so that we can
        calculate its area and perimeter.
        """
    def __str__(self):
        return "It is a polygon with %s sides." % (self.num_sides)
x = Polygon(num_sides = '4')
print(x)

class Rectangle(Polygon):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)
    
H= int(input('Please Enter the Length of the Rectangle: '))
W= int(input('Please Enter the Width of the Rectangle: '))  
 
y = Rectangle(H,W) 
area_result = y.area()
perimeter_result = y.perimeter()

print('-'* 40)
print("Area of Rectangle  = %d" %area_result)
print("Perimeter of Rectangle  = %d" %perimeter_result)
print('__' * 20)

class Square(Rectangle):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        return self.side_length * self.side_length
    
    def perimeter(self):
        return 4 * self.side_length
    
S = int(input('Please enter the side length of the Square: '))  

z = Square(S)

area_result = z.area()
perimeter_result = z.perimeter()

print('-'* 40)
print("Area of Square = %d" %area_result)
print("Perimeter of Square = %d" %perimeter_result)
