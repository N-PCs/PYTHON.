#program for calculating area of circle
import math
r=float(input("enter the radius of given circle"))
A=math.pi*(r**2)  # u can use pi as 3.14 also .
print(A,"is the area of given circle with radius",r)

# area of circle using function

def circle(r):
    import math
    area=(math.pi*(r**2))
    print("area of given circle with radius",r,"is",area,"square units")
    return area

# or

def circles(r):
    area=(3.14*(r**2))
    print("area of given circle with radius",r,"units is",area,"square units")
    return area
