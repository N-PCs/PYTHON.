# Lists => Sequence of characters enclosed within closed/square brackets []
# Functions used here are mostly similar to that of strings.
# Lists are mutable , strings aren't !

l=["Neel","is","cooking","!"]
print(l)

#returns the datatype of given variable
print(type(l))

#returns length of given list
print(len(l))

#checks if a given argument is present in list or not
print("Neel" in l)
print("as" in l)
print('\n')

#Indexing of a list
#we get IndexError if we take index larger than length of list
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[1:3])
print(l[::-1])

