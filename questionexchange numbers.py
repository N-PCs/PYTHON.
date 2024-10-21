# write a python program to exchange two values using third variable and without using variable

#using third variable
a=5
b=6
c=a
a=b
b=c
print(a,"value of a")
print(b,"value of b")

# without using third variable
a=5
b=10
a,b=b,a
print(a)
print(b)

#or


b=5
a=int(b)
print(a)
a=10
b=int(a)
print(b)

#or 
a=10
b=5
a=a-b
b=a+a
print(a)
print(b)


print(bool(0+0.1j)) # imaginary and real part both should be zero for the output to be False

print(complex(5))
print(int("20"))

# print(float(complex(-1,2))) will show error






