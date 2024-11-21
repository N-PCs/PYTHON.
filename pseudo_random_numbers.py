#using random module
# random.randint() , random.randrange() , random.random() , random.choice() , random.uniform()

import random
print(random.randint(10,100))
#generates random integers between the arguments provided to it
print(random.randrange(10))
print(random.randrange(10,20))

print(random.randrange(100,200,3,))
#first argument is the 'start'
#second argument is the 'stop'
#third argument is the 'step'

for i in range(1,6):
	print(random.randint(10,100))
#prints 5 random number between the arguments

#arguments are the values that we put in the parentheses of a function

print(random.random())
#prints random floating number smaller than 1

'''	Functions used to print "INTEGERS"

	1.syntax of randrange function
		random.randrange(start,stop,step)
		
	2.syntax of randint function
		random.randint(start, stop) 
'''

print(random.choice("NEELPANDEY"))
#gives any random string literal from the given input
#can be used for string , lists , arrays etc.

print(random.uniform(10,20))
#gives any random floating number between the two arguments

#generate 10 random numbers between 1 to 100 and sort them in ascending order
l=[]
for i in range(1,11):
	l.append(random.randrange(1,100))
	l1=sorted(l)
print(l1)


'''generate 10 random numbers between 1 to 100 and sort them in ascending order 
and search if 50 is in the array using binary search'''

