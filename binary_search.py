#binary search
def bsearch(a,b,low,high):
    mid=(low+high)//2
    for mid in range(low,high):
        if b==a[mid]:
            print("number found in index-->", mid)
            break
        elif b>a[mid]:
            bsearch(a,b,mid+1,high)
            break                                 #recursive function
        elif b<a[mid]  :
            bsearch(a,b,low,mid-1)
            break
    else:
        print("number not found")


a=[5,10,15,30,49,78,110,159,180] #list must be sorted first
print(str(a))
b=int(input("enter the number to be searched--> "))
low=0
high=len(a)
bsearch(a,b,low,high)
