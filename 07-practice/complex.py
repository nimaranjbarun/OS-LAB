import math

class Complex:

	def __init__(self, real, imaginary):
		self.real = real
		self.imaginary = imaginary
		self.arg = math.acos(self.real/self.mod())

	def __add__(self, no):
		return Complex(self.real + no.real, self.imaginary + no.imaginary)

	def __sub__(self, no):
		return Complex(self.real - no.real, self.imaginary - no.imaginary)

	def __mul__(self, no):
		return Complex(self.real*no.real-self.imaginary*no.imaginary, self.real*no.imaginary+self.imaginary*no.real)

while True : 
    num = input("enter your complex number(like == 5 2) :").split(" ")
    num = complex(int(num[0]),int(num[1]))
    num1 = input("enter your complex number(like == 5 2) :").split(" ")
    num1 = complex(int(num1[0]),int(num1[1]))
    choose = int(input("1.sum\n2.multiply\n3.sub\nyour choice : "))
    if choose == 1 : print(num.__add__(num1))
    elif choose == 2 : print(num.__mul__(num1))
    elif choose == 3 : print(num.__sub__(num1))
    else : break
    