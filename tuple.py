# Tuples => Sequence of characters enclosed within open/round bracket ()
#			They are immutable.

t=(1,2,3,4,5,6,7,1,1,1,2,3)

#printing the elements of tuples
for i in t:
	print(i,end=" ")
print()

for i in range(len(t)):
	print(t[i],end=" ")

print('\n')

#Indexing a tuple
print(t[1])

#Checking the datatype
print(type(t))

#Returns number of occurrences of an argument
print(t.count(1))

#Multidimensional tuples
t=((1,2,3),(4,5,6),(7,8,9),[100,101,102])
print(t[0])
print(t[0][1])  #returns elements inside multidimensional list
print('\n')
#creatin a matrix using tuple
'''for i in range(len(t)):
	for j in range(len(t)):
		print(t[i][j],end=" ")
	print()'''

t[3][1]=1000
print(t[3])   #updates the list present inside the tuple
for k in range(4):
	print(t[k],end=" ")

'''l=[[1,2,3,4],[20,30],[35, 40 , 42],(100,200,300)]
l[3][0]=101                        # U cannot update a tuple present inside a list
print(k[3][0])
'''






