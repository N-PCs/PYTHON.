list2=[]
n=int(input("enter how many numbers you want to add?"))

for i in range(0,n):
	p=eval(input("enter element"))
	list2.append(p)

for i in range (0,n):
	print(list2[i])

print(len(list2))