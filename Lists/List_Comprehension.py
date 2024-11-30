
# Creating a list for multiple of 7
multiples = []
for x in range(1,11):
  multiples.append(x*7)

print(multiples)

#Using list comprehension in Python
#List comprehensions let us create new lists based on sequences or ranges.

multiples=[x*7 for x in range(1,11)]
print(multiples)

#using this method , the code can be written in just one line.

'''Q1: Say we have a list of strings with the names of programming languages,
 	   like this one, and we want to generate a list of the lengths of the strings.'''
#SOLUTION
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths=[len(x) for x in languages]
print(lengths)


#We can also add conditions while utilising list comprehension.
three=[x for x in range(1,101) if x%3==0]
print(three)    #prints multiple of 3 <100

#Use list comprehension for simple code
#Use for loop for complex code
''' Which one will make my code both clear and concise and
 	which one will make my code easier for other people to read and understand? '''
#The answer to the above question must be the most efficient way to iterate lists.


### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines of code into one line:
print([x*2 for x in range(1,11)])

### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code shown below:
my_list = []
for x in range(1,11):
    my_list.append(x*2)
print(my_list)

# Select Run to compare the two results.
print(('\n'))

print("List comprehension result:")
print([x for x in range(1,101) if x % 10 == 0])

# The list comprehension above accomplishes the same result as
# the long form version of the code:
print("Long form code result:")
my_list = []
for x in range(1,101):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)

# Select Run to observe the two results.
print("\n")
#Using list comprehension to print a list of square
def squares(start,end):
	return print([n**2 for n in range(start,end+1)])

squares(1,10)
