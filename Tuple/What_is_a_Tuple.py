# Tuples => Sequence of elements enclosed within open bracket/ parentheses () .
# Similar to lists , but have one major difference ; Tuples are immutable while lists are mutable.

''' Tuples are used in cases where we want to make sure an element in a
	certain position or index refers to one specific thing and won't change.'''

'''Tuples are used for lots of different things in Python. 
	One common example is the return value of functions.
 	When a function returns more than one value, it's actually returning a tuple'''

fullname=("Neel","V","Pandey")
print(fullname)
print(type(fullname))
print("\n")


# tuple() operator
# Convert a list to a tuple
my_list = [1, 2, 3, 4]
print(my_list)
print(type(my_list))
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))
print('\n')

# Remember that although parentheses are often used to define a tuple,
# they're not always necessary. The following syntax is also valid:

my_tuple = 1, 2, 3, 4
print(my_tuple)  # Outputs: (1, 2, 3, 4)


#seconds into hours , minutes , seconds
def convert_seconds():
	seconds=int(input("Enter the number of seconds:"))
	hours=seconds//3600
	minutes=(seconds-(hours*3600))//60
	remaining_seconds=seconds-(hours*3600)-(minutes*60)
	return hours,minutes,remaining_seconds
result=convert_seconds()
print(result)	#returns output as tuple
print(type(result))


# Unpacking a tuple
hours,minutes,remaining_seconds=result
print(hours,"hours",minutes,"min",remaining_seconds,"s")


#Another way to unpack
hours,minutes,remaining_seconds=convert_seconds()
print(hours,"hours",minutes,"min",remaining_seconds,"s")