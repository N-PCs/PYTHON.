#List : Series of comma separated characters enclosed within square/closed bracket []

list1=[1,2,3,4,5,6,7,8,9,10]
list1.append(11)            # adds element at the end of the list
print(list1)
list1.remove(10)            #compares and removes the first element equal to the argument
print(list1)

print(list1[0])     	#prints element at given index
print(list1[2:4])    	#prints set elements
print(list1[::-1])  	#prints in reverse list
print(list1[-6:-1]) #printing with negative indexing

print('\n')

#multidimesional lists
l3=[[1,2,3],[4,5,6],[7,8,9]]

#printing multidimensional list

for i in range(0,3):
	for j in range(0,3):
		print(l3[i][j],end=' ')
	print()
print()



