#!/usr/bin/env python

from random import randint

class Rectangle:
    """This is a Rectangle class which has two different members"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calcArea(self):
        '''
        Function : calculate the area of the Rectangle

        :parameter int width: The width of the Rectangle
        :parameter int height: The height of the Rectangle
        :return: area of the Rectangle
        :rtype: int
        '''
        area = self.width * self.height
        return area

def main ():
    '''
          The main method
    '''

    for i in range(1,6) :
        rect = Rectangle(randint(1,100), randint(1,100))
        area = rect.calcArea()
        print("%d Trial : "%i, "Width =",rect.width , "Height =",rect.height , "Area =",area)

if __name__ == '__main__':
    main()