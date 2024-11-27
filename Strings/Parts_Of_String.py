
# String => Sequence of characters enclosed within quotes.
print("Hello World")
print("This is N-PCs")
print("Here to rule the World !")

# len() function => returns the number of character present in given datatype.
p="Neel Pandey"
print(len(p))
print(p)

# Concatenation => Method in which multiple strings are combined and printed.

a="N-PCs"
b="Gonna rule this world "
c=a+" a.k.a Neel "+b+"!"    #multiple strings added
print(c)
print(c + " \nHe is going to become the King !")

#Accessing elements of string.
#Indexing is used to access the elements of string.
#Positive indexing starts from 0 and ends at len(string)
#Negative indexing starts from -1 to -[len(string)]


d=('''He is known for his intellectual prowess and
he has got some pretty nice vision too !''') #multiple line string (triple quotes used
print(len(d))
print(d)
print(d[20:33])  #doesn't include 33rd index
print(d[-17:-5])
print(d[-24:-18])   #Slicing => accessing slice of string
print(d[-5:])
print(d[:5]+d[5:])  #Combining slices of string

#we can only access elements upto len(string)-1
#print(d[1000]) will show error as the index is out of range i . e length of string.


#Slice => Portion of string that contains more than one character;a.k.a substring.


