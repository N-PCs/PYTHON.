#example

fruits = ["Pineapple", "Banana", "Apple", "Melon"]

#ways to add elements in a list
fruits.append("Kiwi")  #adds the element at the end of the list
print(fruits)

fruits.insert(0, "Orange")  #adds element at any desired index
print(fruits)
fruits.insert(25, "Peach")  #if the index is greater than length of list , it gets added at the end .
print(fruits)

#ways to delete elements from list
fruits.remove("Melon")  #removes the first element equal to the argument
print(fruits)

fruits.pop(3)		#removes element at any desired index
print(fruits)

#updating elements of list
fruits[2] = "Strawberry"  #changes element at index 2 with the argument
print(fruits)