import math
from nis import match

def sum(): print("******************\na + b : " + str(int(input("insert a : "))+int(input("insert b : "))) + "\n******************\n")
def sub(): print("******************\na - b : " + str(int(input("insert a : "))-int(input("insert b : "))) + "\n******************\n")
def multiply(): print("******************\na * b : " + str(int(input("insert a : "))*int(input("insert b : "))) + "\n******************\n")
def divide(): print("******************\na / b : " + str(int(input("insert a : "))/int(input("insert b : "))) + "\n******************\n")
def pow(): print("******************\na ^ b : " + str(int(input("insert a : "))**int(input("insert b : "))) + "\n******************\n")
def sin(): print("******************\nsin(a) : " + str(math.sin(math.radians(int(input("insert angle : "))))) + "\n******************\n")
def cos(): print("******************\ncos(a) : " + str(math.cos(math.radians(int(input("insert angle : "))))) + "\n******************\n")
def tan(): print("******************\ntan(a) : " + str(math.tan(math.radians(int(input("insert angle : "))))) + "\n******************\n")
def cot(): print("******************\ncot(a) : " + str(1 / math.tan(math.radians(int(input("insert angle : "))))) + "\n******************\n")
def Bye(): exit("Bye!!!")
options = {0 : Bye,1: sum,2: sub,3 : multiply,4 : divide,5 : pow,6 : sin,7 : cos,8: tan,9 : cot};
while True : 
    print("\n\n1.sum | 2.sub | 3.multiply | 4.divide | 5.pow | 6.sin | 7.cos | 8.tan | 9.cot | 0.Bye\n\n");
    options[int(input("insert your function number : "))]()
     
