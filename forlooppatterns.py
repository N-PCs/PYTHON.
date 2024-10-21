"""prints pattern like this *
                            **
                            ***
                            ****
                            *****"""
n=int(input("enter a number--> "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()


'''prints pattern like 1
                       12
                       123
                       1234'''
n=int(input("enter a number--> "))
for i in range(1, n+1):
    for j in range(1, i+1):
      print(j, end="")
    print()

'''prints pattern like 1
                       23
                       456
                       78910'''

n=int(input("enter a number--> "))
k=1
for i in range(1, n+1):
    for j in range(1, i+1):
      print(k, end="")
      k=k+1
    print()


'''prints pattern like 1
                       22
                       333
                       4444'''
n=int(input("enter the number--> "))
i=1
for i in range(1, n+1):
      print(i*str(i), end="")

      print()

          # OR #

n=int(input("enter the number--> "))
j=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

