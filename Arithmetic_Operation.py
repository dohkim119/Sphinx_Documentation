#!/usr/bin/env python

from random import randint

class Number:


    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

def addition(num1, num2):

    sum = num1 + num2
    return sum

def subtraction(num1, num2):

    sub = num1 - num2
    return sub

def multiplication(num1, num2):

    mul = num1 * num2
    return mul

def division(num1, num2):

    div = num1 / num2
    return div


def main ():

    i = 0
    area = 0

    for i in range(1,6) :
        num = Number(randint(1,100), randint(1,100))
        sum = addition(num.num1, num.num2)
        sub = subtraction(num.num1, num.num2)
        mul = multiplication(num.num1, num.num2)
        div = division(num.num1, num.num2)
        print("%d Trial : "%i, "Num1 =",num.num1 , "Num2 =",num.num2)
        print("\t Sum = %d  Sub = %d  Mul = %d  Div = %.2f"%(sum,sub,mul,div))

if __name__ == '__main__':
    main()
