a=int(input("enter first num"))
b=int(input("enter second num"))
c=int(input("enter third num"))

if a>b and a>c:
    print(a,"is the largest ")
elif b>c and b>a:
    print(b," is the largest")
else:
    print(c,"is the largest")
