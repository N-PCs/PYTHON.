# numerical types
a=3+4j
b=3+4.2j
c=0b1011010+5j     #binary with complex
d=0o345+4j         #octal with complex

e=d+c
f=d*c
print(b)
print(a)
print(c)
print(d)
print(e)
print(f)


#type casting 
#eg
b=30.5 #float object uses 24 bytes
a=15    #an integer occupies four bytes, or 32 bits
a=b # type casting
b=a
print(a)
print(b)

# two types of type casting implicit and explicit
#implicit type casting is done by computer while converting from one data type to other
#explicit type casting is done by humans manually while converting from one data type to other
print(int(123.5))
print("10")
print(int("10"))
#  print(int("ten")) will show error
#  print(int("10.2")) will show error

print(int(0o34))
print(int(0b1011010))  #converts binary to decimal

print(float(True))  # float with boolean variables

print(int(False))

print(complex(84))  #complex with decimal
print(complex(10,-2)) # way to represent complex number

# non zero values are always True(decimal and integer)
# only zero will give False (decimal and integer)

print(bool(7))
print(bool(0))

print(bool(9.7))
print(bool(0.0))

#complex number will only give False if both the imaginary and real parts are zero
print(bool(complex(0,0)))

# all string will show True except if it is empty string
# empty string will give False
print(bool("string"))
print(bool(""))

#string

print(str(19.0))
print(str(67))
print(str(complex(10,-6)))


# some escape characters
#  \n    new line
#  \t    horizontal tab 


def fun(a,b):
    c=a*b
    return c





