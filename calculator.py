#calculator
z=input("which operation do you want to perform + - / * ^ enter  ")
if z=="+":
    l=float(input("enter the number"))
    m=float(input("enter the number"))
    n=l+m
    print(l,"+",m,"=",n)

elif z=="-":
    l=float(input("enter the number"))
    m=float(input("enter the number"))
    n=l-m
    print(l,"-",m,"=",n)
    
elif z=="/":
    l=float(input("enter the number"))
    m=float(input("enter the number"))
    n=l/m
    print(l,"/",m,"=",n)

elif z=="*":
    l=float(input("enter the number"))
    m=float(input("enter the number"))
    n=l*m
    print(l,"*",m,"=",n)
    
elif z=="^":
     l=float(input("enter the number"))
     m=float(input("enter the number"))
     n=l**m
     print(l,"**",m,"=",n)
    
