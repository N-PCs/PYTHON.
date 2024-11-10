n=int(input("enter the number--> "))
a=0
b=1
print(a)
print(b)
for i in range(1,n-1):
    s=a+b
    print(s)
    a=b
    b=s
