"""prints pattern like this *
                            **
                            ***
                            ****
                            *****"""
n=int(input("enter a number--> "))
i=0
while(i<=n):
    j=0
    while(j<=i):
        print("*",end="")
        j=j+1
    print("")
    i=i+1




"""prints output as 1
                     2 3
                     4 5 6
                     7 8 9 10"""
m=int(input("enter a number--> "))
i=0
k=1
while(i<=m):
    j=1
    while(j<=i):
        print(k,end=" ")
        j=j+1
        k=k+1
    print()
    i=i+1


"""prints """

l=int(input("enter a number--> "))
i=1
for i in range(1, l+1):
      print(i*str(i), end="")

      print()


