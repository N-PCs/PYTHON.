t1=((1,2),(3,4))
t2=((5,6),(7,8))
t3=([0,0],[0,0])	#Create a empty list inside tuple so that we can edit it and add the result

for i in range(2):
	for j in range(2):
		t3[i][j]=t1[i][j]+t2[i][j]

for i in range(2):
	for j in range(2):
		print(t3[i][j],end= " ")
	print()
