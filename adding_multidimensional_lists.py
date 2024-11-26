#adding multiple multidimensional lists
l4=[[1,2,3],[4,5,6],[7,8,9]]
l5=[[9,8,7],[6,5,4],[3,2,1]]
l6=[[0,0,0],[1,1,1],[2,2,2]]

for i in range(0, 3):
	for j in range(0, 3):
		print(l4[i][j], end=' ')
	print()
print()

for i in range(0, 3):
	for j in range(0, 3):
		print(l5[i][j], end=' ')
	print()
print()


for i in range(0,3):
	for j in range(0,3):
		l6[i][j]=l4[i][j]+l5[i][j]


print("Addition of the given lists =>")
for i in range(0,3):
	for j in range(0,3):
		print(l6[i][j],end=' ')
	print()

