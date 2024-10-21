# RightShift operator (>>)
# Leftshift operator(<<)

c=32<<2
print(c)

print(bin(20))
d=20<<2 #i.e 20* (2**2)
print(d)

d=20<<3 #20*(2**3)
print(d)

e=20>>2
print(e) # i.e 20/(2**2)

a=12>>3

print(a)

#multiple assignment operator(specific only to python)

a,b,c=10,20,30
print(a)
print(b)
print(c)

# identity operator
# is and is not

a=10
b=20
print(a is b)
print(a is not b)
print(id(a)) #id function

# member ship operator
#checks within list , tuples, strings, dictionary

y="hello world"
print("h" in y)
print("" not in y)
print("s" not in y)
