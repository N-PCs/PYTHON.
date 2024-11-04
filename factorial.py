#factorial question
import math
def factorial(a):
    import math
    if a>1:
        c=math.factorial(a)
        print(a,'! is equal to',c)
    elif a==0 or a==1:
        print("factorial is 1")
    else:
        print("factorial doesn't exists for negative numbers")


# OR
#using loop only

n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    f = 1
    for i in range(1, n + 1):
        f *= i
    print("the factorial of given number",n,"is ",f)


# without function
n=int(input("enter the number-->"))
import math
if n>1:
    print("the factorial of given number",n,"is = ",math.factorial(n))
elif n==1 or n==0:
    print("factorial is = 1 ")
else:
    print("factorial doesn't exist for negative numbers")
        

