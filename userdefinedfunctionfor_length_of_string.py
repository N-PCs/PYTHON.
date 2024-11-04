#create a user defined function to calculate length of string
def length(l):
    count=0
    for i in l:
        count=count+1
    print(count)
l=str(input("enter the string--> \n"))
length(l)
print("Is the length oif given string :)")


