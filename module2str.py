print("hello world")

import keyword
print(keyword.kwlist) # shows list of keywords available in python


a=2
b=3
c=a*b
print(c)
list=[2,3,4,5,50]
print(list[2])
str="neelpandey"
print(str[4])

a=3
print(type(a))

d=10+3j
e=5+6j
f=d*e
print(f)

a=0x56
print(bin(a))
print(a)
print(oct(a))

b=0B1010110
print(b)

a1=True
b1=False
if (a1!=b1):
    print(type(b1))
    print(b1)
    
else:
    print(a1)

g=10 
h=11 
print(g==h)
print(g!=h) #checking if g and h are equal or not

# there are 33 keywords
# only 3 are exceptions true false none

#String Operations
string="neel"
print(string)
print(string[1:3])   # this process is known as slicing
# indexing starts from 0 for left to right i.e positive indexing
#indexing starts from 1 for right to left i.e negative indexing

print(string[-1:-3])


str="vit bhopal university"
print(str[0])
print(str[-19:-2])



print(len(str)) #this is len function its is used to find length of the strings

print(str[0:15]) #here it inludes 15 thus it prints from index 0 to 14
print(str[-21])      #negative indexing


print(str*2)  #string multiplication ?/ repetition

#slicing: some part of string is obtained by indexing it

#three types of numbers in python are integer,float(decimal+number),complex number








