#this program finds the smallest common divisor of given number
m= int(input("enter greater number-> "))
n= int(input("enter smaller number-> "))
for i in range(2,m+1):
	if m%i==0 and n%i==0:
		print(i)
		break
else:
	print("no common divisor")