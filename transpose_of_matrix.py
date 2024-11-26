print("MATRIX =>")
m=int(input("enter number of rows -> "))
n=int(input("enter number of columns -> "))


#print list 1
l1=[[0 for n in range(n)] for m in range(m)]
print("Enter elements for first matrix")
for i in range(0,m):
	for j in range(0,n):
		x=int(input())
		l1[i][j]=x

print("Input Matrix !")
for i in range(0,m):
	for j in range(0,n):
		print(l1[i][j],end=" ")
	print()
print()

print("Transpose of given matrix :) ")
for i in range(0,n):
	for j in range(0,m):
		print(l1[j][i],end=" ")
	print()
print()

