from typing import Type
#Import math Library
import math

class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def print(self):
        print(self.numerator,"/", self.denominator)        

    def plus(self, f):
        if(self.denominator!=f.denominator):
            gcd1 = math.gcd(self.denominator, self.numerator)
            gcd2 = math.gcd(f.denominator, f.numerator)
            return (self.numerator*gcd2 + f.numerator*gcd1)/(gcd1*gcd2)
        else:
            return (self.numerator + f.numerator)/(self.denominator)

    def minus(self, f):
        if(self.denominator!=f.denominator):
            gcd1 = math.gcd(self.denominator, self.numerator)
            gcd2 = math.gcd(f.denominator, f.numerator)
            return (self.numerator*gcd2 - f.numerator*gcd1)/(gcd1*gcd2)
        else:
            return (self.numerator - f.numerator)/(self.denominator)

    def multipliedBy(self, f):
        return (self.numerator*f.numerator)/(self.denominator*f.denominator)

    def dividedBy(self, f):    
        return (self.numerator*f.denominator)/(self.denominator*f.numerator)


f1 = Fraction(46,60)
f1.print()
f2 = Fraction(12,60)
f2.print()

print("suma:"+str(f1.plus(f2)))
print("minus:"+str(f1.minus(f2)))
print("multipliedBy:"+str(f1.multipliedBy(f2)))
print("dividedBy:"+str(f1.dividedBy(f2)))
