num = int(input("Enter a number: "))

if num <= 1:
  print(num, "is not a prime number.")
else:
  is_prime = True
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      is_prime = False
      break

  if is_prime:
    print(num, "is a prime number.")
  else:
    print(num, "is not a prime number.")


# OR

n=int(input("enter the number : "))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
    if(i==n-1):  #---->>  importance of break : it saves the program from running the same statement multiple times
        print("number is prime")


# OR
n=int(input("enter the number : "))
i=1
while(i<n-1):
    i=i+1
    if(n%i==0):
        print("number is not prime")
        break
else:
    print("number is prime")


#OR
a=int(input("enter a number--> "))
count=0
for i in range(1,a+1):
    if a%i==0:
        count=count+1
        i=i+1
if count==2:
    print("prime number :) ")
else:print("not prime :(")





