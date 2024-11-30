#iterating a list
n=[1,2,3,4,5,6,7,8,9]
for i in n:
	print(i,end=" ")
print('\n')

#iterating a list with a tuple as element
m=[(1,2,3),(4,5,6),(7,8,9)]
for i in m:
	print(i,end=" ")
print('\n')

# iterating a list with a list as element
k=[[1,2,3],[4,5,6],[7,8,9]]
for i in k:
	print(i,end=" ")
print('\n')

#iterating a list with both tuple and list as element
j=[[1,2,3],(4,5,6),[7,8,9],(10,11,12)]
for i in j:
	print(i,end=" ")
print('\n')

#iterating a list with a string as element
p=["Neel","V","Pandey","a.k.a","N-PCs","is","the","G.O.A.T"]
for i in p:
	print(i,end=" ")
print('\n')


#Example1
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
	chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))


#Example 2:
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
	print("{} - {}".format(index + 1, person))


# enumerate function:
''' The enumerate function returns a tuple for each element in the list. 
	The first value in the tuple is the index of the element in the sequence. 
	The second value in the tuple is the element in the sequence.'''

#Example 3
def full_emails(people):
	result = []
	for email, name in people:
		result.append("{} <{}>".format(name,email))
	return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))
