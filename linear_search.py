a=[10,67,5,23,59,20,81,99,51]
print(str(a))
b=int(input("enter the number to be searched from the list--> "))
for i in range(0,len(a)):
    if a[i]==b:
        print("number found in index--> ",i)
        break
else:
    print("number not found")



#three types of complexity in linear search
        #best : order of 1 i.e O(1)
        #avg: O(n)
        #worst :O(n)

# three types of complexity in binary search
# best : order of log1 i.e O(log(1))
# avg: O(log(n))
# worst :O(log(n))


a=[10,67,5,23,59,20,81,99,51]
def linears(a,b):
    for i in range(0,len(a)):
        if(a[i]==b):
            print("number is found",i)
            break
    else:
        print("number not found")

print(str(a))
b=int(input("the number to be searched"))



