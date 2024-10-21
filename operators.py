#OPERATORS
#Aritrhmetic, comparison, logical, bitwise, identity, augmented assignment operator

#operators precedence is PEMDAS
#  Parentheses,exponent,multiplication, division, addition, subtraction


#Arithmetic operators
#unary , binary , turnary
#unary= acts on one number  ; binary = acts on two number ; turnary= acts on three variable

#unary eg=  +a
#binary  eg= a+-/*b

print(5/2) #division
print(5//2) #floor division
print(5**2) # exponent
print(5%2)  #modulus

a=5
b=++a #pre increment
c=--a #pre decrement
print(a)
print(b)
print(c)




a=5
b=++a
print(a)
print(b)
c=--a
print(a)
print(c)

print(a==b)
print(a!=b)

print(a>=b)
print(a<=b)



a=5 # comparison operator
b=++a
print(a)
print(b)
c=--a
print(a)
print(c)

print(a==b)
print(a!=b)

print(a>=b)
print(a<=b)


#Logical operator
# not (negation), and (multiplication), or (addition)
a=True
b=False
print(not a)
print(not b)

print(a or b)
print(a and b)
x=0
print(not x)
y=12
print(not y)

###########

x=10
y=20
z=30

a=x>y or y<z

print(a)

b=x<y or x<z or y<z
print(b)

c= x>y and y<z
print(c)

d=x<y and y<z
print(d)

# Bitwise Operator
# works on bit by bit

g=10
h=20

# 01010 & 10100 = 00000
# in bitwise operation 0 &1=0

# bitwise and
i=g&h
print(i)
print(bin(i))


a=12
b=15
c=a&b
print(c)
print(bin(c))
print(bin(a))
print(bin(b))


#bitwise  or 

d=a|b
print(d)

# bitwise negation ~
e=~a
print(e)

# eg   1100
#      |
#      most significant digit 

print(~5)

#exlcusive or(XOR) a^b  also known as bitwise XOR

j=a^b
print(j) 

k=1
l=0
m=l^k
print(m)








