print("MATRIX 1 =>")
m=int(input("enter number of rows -> "))
n=int(input("enter number of columns -> "))
print('\n')
print("MATRIX 2 =>")
p=int(input("enter number of rows -> "))
q=int(input("enter number of columns -> "))
print('\n')
if n==p:

#print list 1
	l1=[[0 for n in range(n)] for m in range(m)]
	print("Enter elements for first matrix")
	for i in range(0,m):
		for j in range(0,n):
			x=int(input())
			l1[i][j]=x
	print('\n')
#print list 2
	l2=[[0 for q in range(q)] for p in range(p)]
	print("Enter elements for second matrix")
	for i in range(0,p):
		for j in range(0,q):
			y=int(input())
			l2[i][j]=y
	print('\n')
#list 3 for storing their multiplication values
	l3=[[0 for q in range(q)] for m in range(m)]
	for i in range(0, m):
		for j in range(0, q):
			for k in range(0, n):
				l3[i][j] = l3[i][j] + l1[i][k] * l2[k][j]   #main code to utilise here



#Printing the matrices and their multiplication
	for i in range(0,m):
		for j in range(0,n):
			print(l1[i][j],end=" ")
		print()
	print()

	for i in range(0,p):
		for j in range(0,q):
			print(l2[i][j],end=" ")
		print()
	print()

	for i in range(0,m):
		for j in range(0,q):
			print(l3[i][j],end=" ")
		print()
	print()




else:
	print('Matrix cannot be multiplied!')
	print('\nReason :')

	print("Because number of columns of matrix 1 \nis not equal to number of rows of matrix 2 !")

#The number of columns in Matrix A (𝑛) must be equal to the number of rows in Matrix B (𝑛).