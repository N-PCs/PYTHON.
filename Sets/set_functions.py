numbers={1,2,3,4,5,6,7,8,9}


# DELETING ELEMENTS OF SET :

# Using discard() function => deletes the first number equal to the argument
numbers.discard(7)
print(numbers)    #OUTPUT : {1,2,3,4,5,6,8,9}
# if the argument doesn't lie in the given set , the discard function simply ignores it.
numbers.discard(10)
print(numbers)	  #OUTPUT : {1,2,3,4,5,6,8,9}
print('\n')

# Using remove() function => deletes the first number equal to argument
num={2,4,6,8,10,12,14}
num.remove(12)
print(num)
# if the argument doesn't lie in the given set , the discard function simply ignores it.
print('\n')

# Using pop() function => deletes the first element
num.pop()
print(num)
print('\n')

# Using clear() functions => removes all the elements of the set
# returns empty set
num.clear()
print(num)
print(type(num))
print('\n')

'''-----------------------------------------------------------------------------------------------------------------'''

# UPDATING THE ELEMENTS OF SET :

# Using add() function => adds element at the end of set
n={1,2,3,4,5,6,7,8,9}
n.add(10)
print(n)
print('\n')

# Using update() function => can add multiple elements
n.update({11,12,13,14,15})
print(n)
n.update([16,17,18])		#can add list elements too!
print(n)
print('\n')

# len() => returns length of set
print(len(n))
print('\n')

# sorted() => returns sorted set
s={1,4,2,3,6,9,7,8}
s=sorted(s)
print(s)
q={0}
print('\n')

# any() => returns True if there is at least one non-zero element in set
print(any(s))
print(any(q))
print('\n')

# all() function => returns true if all elements in a set are non-zero
print(all(s))
print(all(q))
print('\n')

'''---------------------------------------------------------------------------------------------------------'''

#SET OPERATIONS

# union function => adds all the elements of two sets
j={1,2,3,4,5,6,7,8,9}
k={10,11,12,13,14,15,1,2}
print(k.union(j))
print('\n')

# intersection() function => returns common elements from two sets
print(k.intersection(j))
print('\n')

# difference() function => gives elements of one set removing the common elements from other sets
print(k.difference(j))
print(j.difference(k))
print('\n')

# symmetric difference() function => removes the common elements and adds all the unique elements
print(k.symmetric_difference(j))
print(j.symmetric_difference(k))
print('\n')

# difference_update() function
print(j.difference_update(k))
print(k.symmetric_difference(j))
print('\n')

# symmetric_difference_update() function =>
j = {1, 2, 3, 4, 5, 6, 7, 8, 9}
k = {10, 11, 12, 13, 14, 15, 1, 2}
j.symmetric_difference_update(k)  #updates set j to be the symmetric difference of j and k
print("Updated set j:", j)
k.symmetric_difference_update(j)  #updates set k to be the symmetric difference of j and k
print("Updated set k:", k)  
print('\n')

# isdisjoint() function => returns True if there are no common elements between two sets
j={1,2,3,4,5,6,7,8,9}
k={10,11,12,13,14,15,1,2}
print(k.isdisjoint(j))
print('\n')

# issubset() function = checks if a given function is a subset of another set
print({1,2}.issubset({1,2,3,4,5}))
print({6,7}.issubset({1,2,3,4,5}))
print('\n')

# issuperset() function => checks if a given set is superset of another set
print({2,4,8,10}.issuperset({2,4}))
print({2,4,8,10}.issuperset({1,2,3,4}))


