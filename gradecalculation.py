# grade calc.
N=input("enter name  ")

p=float(input("enter marks in phy  "))
c=float(input("enter marks in chem  "))
b=float(input("enter marks in bio  "))
av=(p+c+b)/3
print(av,"is the percentage")
if av>90:
    print(N,"has got S grade")
elif av>80:
    print(N,"has got A grade")
elif av>70:
    print(N,"has got B grade")
elif av>60:
    print(N,"has got C grade")
elif av>50:
    print(N,"has got D grade")
elif av>40:
    print(N,"has got E grade")
else:
    print(N,"has got Fail grade")


# using function
def grade(p,c,b):
    N=input("name  ")
    av=(p+c+b)/3
    print(av)
    if av>90:
        print(N,"has got S grade")
    elif av>80:
        print(N,"has got A grade")
    elif av>70:
        print(N,"has got B grade")
    elif av>60:
        print(N,"has got C grade")
    elif av>50:
        print(N,"has got D grade")
    elif av>40:
        print(N,"has got E grade")
    else:
        print(N,"has got Fail grade")
        
        
# using function but without parameters
def grades():
    N=input("name  ")
    p=float(input("enter marks in phy  "))
    c=float(input("enter marks in chem  "))
    b=float(input("enter marks in bio  "))
    av=(p+c+b)/3
    print(av,"is ",N,"'s percentage")
    if av>90:
        return(N,"has got S grade")
    elif av>80:
        return(N,"has got A grade")
    elif av>70:
        return(N,"has got B grade")
    elif av>60:
        return(N,"has got C grade")
    elif av>50:
        return(N,"has got D grade")
    elif av>40:
        return(N,"has got E grade")
    else:
        return(N,"has got Fail grade")
    
    
    
   
        


    
