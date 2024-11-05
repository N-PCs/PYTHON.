a=int(input("Enter the number --> "))
l=["1","One","2","Two","3","Three","4","Four","5","Five","6","Six","7","Seven","8","Eight","9","Nine","0","Zero"]
b=str(a)
for i in b:
    if i in l:
        c=l.index(i)
        print(l[c+1],end=" ")
print("\n")


#OR
d=input("Enter the number --> ") # u can directly take the number as input without using int(input())
l=["1","One","2","Two","3","Three","4","Four","5","Five","6","Six","7","Seven","8","Eight","9","Nine","0","Zero"]

for i in d:
    if i in l:
        c=l.index(i)
        print(l[c+1],end=" ")
print("\n")


a=input("Enter the number --> ")
l=["1","2","3","4","5","6","7","8","9","0"]
for i in a:
    if i in l:                                               #using simpler functions and loops
        if i=="0":
            print("Zero",end=' ')
        elif i=="1":
            print("One",end=' ')
        elif i=="2":
            print("Two",end=' ')
        elif i =="3":
            print("Three",end=' ')
        elif i=="4":
            print("Four",end=' ')
        elif i =="5":
            print("Five",end=' ')
        elif i =="6":
            print("Six",end=' ')
        elif i =="7":
            print("Seven",end=' ')
        elif i =="8":
            print("Eight",end=' ')
        elif i =="9":
            print("Nine",end=' ')

print("\n")
