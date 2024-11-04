def find_sld(n):
    num_str = str(n)
    ld = -1
    sld = -1
    for i in num_str:
        digit = int(i)
        if digit > ld:
            sld = ld
            ld = digit
        elif digit > sld:
            sld = digit

    return sld

n=int(input("enter the numnber --> "))
print(find_sld(n),"is the second largest digit of given number")


#
m=int(input("enter the number--> "))
strn=str(m)
ld=0
sld=0
for i in strn:
    digit=int(i)
    if digit>ld:
        sld=ld
        ld=digit
    elif digit>sld:
        sld=digit

print(sld, "is the second largest digit of given number" )


