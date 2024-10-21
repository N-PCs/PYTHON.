# module 
#one module stores classes, functions etc.
#can be made available to interpreter by using 'import' statement
#module are of two types : user defined and library modules

def oddeven(a):
    if a%2==0:
        print(a," the number is even ")
    else:
        print(a,"number is odd")

#built in modules
''' eg: platform module , system module , math module , statistic module'''

import platform
x=platform.system() # gives output as the operating system used by the person
print(x)

import math as d 
print(d.ceil(5.2)) #smallest number greater than the given number
print(d.floor(5.2)) #largest number smaller than the given number 
print(d.sqrt(4))   # square root
print(pow(2,3))  # prints x^y i.e here 2^3=8






    