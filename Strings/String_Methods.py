a=" This file is made by N-PCs "
print(len(a))
print(a.count("i")) #returns the number of occurrences of argument in string
print(a.find("a"))	#returns index of argument

print('\n')

print(a.upper())	#converts string to uppercase.
print(a.lower())	#converts string to lowercase.
print(a.title()) 	#converts each starting letter of word in a string to uppercase.
print(a.capitalize())  #transforms the first character of a string to uppercase while converting all remaining characters to lowercase.
print(a.swapcase())  #swaps uppercase to lowercase and vice versa
print(a.replace("file","folder")) #used to replace some part os string with other substring
print('\n')

print(a.strip())    #gets rid of any extra whitespaces.
print(a.lstrip()) 	#removes whitespaces on L.H.S
print(a.rstrip()) 	#removes whitespaces on R.H.S

print('\n')

print(a.endswith("N-PCs ")) #returns whether the string ends with a certain substring
print(a.endswith("N-PCs")) #returns false . remember whitespaces also count!
print(a.startswith(" This"))

print('\n')

print(a.isnumeric())	#returns whether the string's made up of just numbers.
print(a.isalpha())      #returns whether the string's made up of just letters.
print(a.isalnum())      #returns whether the string's made up of both numbers and letters.

print('\n')

print(a.split())		#returns a list of all the words in the initial string , and it automatically splits by any whitespace.
#join() method is basically inverse of split method
print(' '.join(a.split()))  #returns original string
