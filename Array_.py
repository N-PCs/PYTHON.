'''# ARRAY
# Operations of array :->
# Index , Traverse , Insert , Delete , Search , Update '''


#creating array
#use numpy
#         OR
'''from array import *  '''
'''Or'''
'''import array
	arr1=array(typecode,[initializer])'''

import array
arr1=array.array('i',[15,20,25,78,50,87])
for i in arr1:
	print(i)


def arrlen(a):
	count = 0
	for i in a:  				# function to find length of any given item
		count = count + 1  		# works only when given object is iterable


	print(count)

arrlen(arr1)

#OR

def userlen(a):
	count=0
	for j in a:
		count= count +1
	return count

userlen(arr1)

'''integers take 4 bytes == 32 bits space'''
'''Typecode are the codes that are used to define the type of 
value the array will hold. '''



'''Some common typecodes used are:
Typecode	Value

   b       	Represents signed integer of size 1 byte (-128- 
			to +127)
   B 		Represents unsigned integer of size 1 
			byte(0-255)
   c 		Represents character of size 1 byte (0-127)
   i 		Represents signed integer of size 4 bytes 
			–(2,147,483,648 to 2,147,483,647)
   I 		Represents unsigned integer of size 4 bytes
   f 		Represents floating point of size 4 bytes
   d 		Represents floating point of size 8 bytes
'''


import array
arr2=array.array('i',[45,25,33,88,51,47])
for i in arr2:
	print(i)
print(arr2[2])         #array indexing
print(arr2[-4])			# negative indexing

# inserting new elements
arr2.insert(0,100)
print(arr2)

#appending new elements
arr1.append(200)
print(arr1)

'''main difference between append and insert is that insert adds elements at any desired position
while append adds a single elemnts at the end of given object'''

#delete elements
#this function deletes the first element that matches the argument

arr3=array.array('i',[20,30,40,50,60,40,50,80])
arr3.remove(40) # will remove the '40' at 2 index and not the one at 5 index
print(arr3)

# or other way to delete is to use del function

del arr1[3]                 # deletes element a given index
print(list(arr1))

#Update elements
arr4=array.array('i',[20,45,87,96,45,35,12,10,25,47])
print(arr4)
arr4[3:5]=array.array('i',[500,501])
print(arr4)

#reverse() function
arr5=array.array('i',[20,15,57,92,42,35,12,10,25,47])
print(arr5)
arr5.reverse()
print(arr5)

#reversed() function

