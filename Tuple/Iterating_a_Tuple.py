#iterating a tuple
n=(1,2,3,4,5,6,7,8,9)
for i in n:
	print(i,end=" ")
print('\n')

#iterating a tuple with a tuple as element
m=((1,2,3),(4,5,6),(7,8,9))
for i in m:
	print(i,end=" ")
print('\n')

# iterating a tuple with a list as element
k=([1,2,3],[4,5,6],[7,8,9])
for i in k:
	print(i,end=" ")
print('\n')

#iterating a tuple with both tuple and list as element
j=([1,2,3],(4,5,6),[7,8,9],(10,11,12))
for i in j:
	print(i,end=" ")
print('\n')

#iterating a tuple with a string as element
p=("Neel","V","Pandey","a.k.a","N-PCs","is","the","G.O.A.T")
for i in p:
	print(i,end=" ")
print('\n')

#example:
def full_emails(people):
	result = []
	for email, name in people:
		result.append("{} <{}>".format(name, email))
	return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))
