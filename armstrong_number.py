# Q1 write a program to print all armstrong number between 100 to 999
# Q2 write a program to print following
               #*****
               #****
               #***
               #**
               #*
# Q3 write a program to convert one decimal number to binary number without using bin function

#SOLUTIONS

#Q1 ans.
for n in range(100,1000):
    a=n//100
    b=(n//10)%10
    c=n%10
    s=(a*a*a)+(b*b*b)+(c*c*c)
    if n==s:
        print(n)


# Q2 ans
n=int(input("enter the number--> "))
for i in range(n,0,- 1):
    print('*'*i)

#OR
n=int(input("enter the number--> "))
for i in range(0,n+1):
    print('*'*(n-i)


# Q3 ANS
def dtob(number):
  binary_string = ""
  while number > 0:
    remainder = number % 2
    binary_string = str(remainder) + binary_string
    number //= 2
  return binary_string

decimal_num = int(input("Enter a decimal number: "))
binary_num = dtob(decimal_num)
print("Binary equivalent:", binary_num)

# this program can be written by recursive function also

















