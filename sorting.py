#bubble sort
#uses two 'for' loops
a=[20,10,5,6,78,8,4,59,62,36,110,115,514]
print(str(a))
c=sorted(a)
print("sorted list: ", c)

def bsort(a):
    for i in range(0,len(a)):
        for j in range(0,len(a)-i-1):
            if (a[j]>=a[j+1]):
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
    for i in range(0,len(a)):
        print(a[i] ,end='  ')
def lsearch(a,b):
    for i in range(0,len(a)):
        if a[i]==b:
            print("number found in index--> ",i)
            break
    else:
        print("number not found")

def bsearch(a,b,low,high):
    mid = (low + high) // 2
    for mid in range(low, high):
        if b == c[mid]:
            print("number found in index-->", mid)
            break
        elif b > c[mid]:
            bsearch(c, b, mid + 1, high)
            break  # recursive function
        elif b < c[mid]:
            bsearch(c, b, low, mid - 1)
            break
    else:
        print("number not found")

inp=input("Enter your choice \n 1. bsearch \n 2. lsearch \n 3. bsort\n 4. exit \n -->")
if inp=="bsearch":
    low=0
    high=len(a)
    b = int(input("number to search--> "))
    bsearch(a,b,low,high)
elif inp=="lsearch":
    b=int(input("enter the number--> "))
    lsearch(a,b)
elif inp=='bsort':
    bsort(a)
elif inp=="exit":
    print("exit the program")

#complexity of bubble sort is O(n^2)

#binary search
#linear search
#sorting
#exit




