# write a program to print all the palindrome number from 100 to 999

for n in range(100,999):
    a=str(n)
    if a==a[::-1]:
        print(n)

#OR

