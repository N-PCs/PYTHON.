#binary search
def bsearch(a,b,low,high):
    c=sorted(a)
    mid=(low+high)//2
    for mid in range(low,high):
        if b==c[mid]:
            print("number found in index-->", mid)
            break
        elif b>c[mid]:
            bsearch(c,b,mid+1,high)
            break                                 #recursive function
        elif b<c[mid]  :
            bsearch(c,b,low,mid-1)
            break
    else:
        print("number not found")


a=[5,10,15,30,49,78,110,159,180]
print(str(a))#list must be sorted first
b=int(input("enter the number to be searched--> "))
low=0
high=len(a)
bsearch(a,b,low,high)
