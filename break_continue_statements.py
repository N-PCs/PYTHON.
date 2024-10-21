# transfer statements
# break, continue , pass

n=int(input("enter a number--> "))
for i in range(1,n+1):
    print(i)
    if i==5:   # output 5 tak hi aayega uske baad break ho jaayega
        print("before break")
        break

        print("after break")  # this code is known as "unreachable code"
    print("end of the loop")
print("end of the loop \n")  #\n is the new line character

##########################################################################
n=int(input("enter a number--> "))
for i in range(1,n+1):
    print(i)
    if i==5:   # output 5 tak hi aayega uske baad break ho jaayega
        continue  #skips all the statements available under it
    print("end of the loop")
print("end of the program")
#---------------------**----------------------------**-------------------------------#





