#write a python program to print the pattern
#                        *
#                       ***
#                      *****
#                     *******

#program
n=int(input("the number of times u want to print this pattern \n   * \n  *** \n *****  ... \n Enter--> "))
for i in range(1,n+1):
        print(" "*(n-i),end='')
        print("* "*i)


n=int(input("enter N"))
f = 1
for i in range(1,n+1):
        f=f*i
1
print("the factorial is",f)



