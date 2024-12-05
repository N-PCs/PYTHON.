# Set = Sequence of elements within braces or curly bracket {}
# is mutable
# doesn't support indexing
# is heterogeneous i . e can contain elements of multiple datatype
# interpreter sorts the elements of set in ascending order


s={1,2,3}
print(s)

a={1,2.0,'three',0+0j}
print(a)				#prints the output in ascending order

b={10,20,30,10,40}
print(b)           		#no repetition of elements allowed

# we cannot define any list , set , dictionary inside a set.
#d={[1,2,3],4} will show error on printing.

#but we can define immutables like tuples , numbers inside a set.
d={(1,2,3),4}
print(d)

# Creating a set using set() function
c=set((1,2,3,4,5,1))  			#converts tuple to set
print(c)
e=set([1,2,3,4,5,1,1])		    #converts list to set
print(e)

# Accessing elements of a set
# We cannot access elements of set using indexing so we use for loop
f={1,4,6,9,7}
for i in f:
	print(i)







