'''pass statement: is a null statement , interpreter doesn't ignore a pass statement ,
but does no operation on it , so it gives no output'''
def add(n1,n2):
    pass
add(1,2) #will give no output

i=0
while i<=10:
    if i==7:
        i=i+1
        continue
    print("the number is :",i)
    i=i+1


