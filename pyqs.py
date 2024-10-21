p=float(input("enter the price of the clothes--> "))
if p>=25000:
    print(p, "price before discount")
    p=p-p*0.5
    print(p,"is the discounted price")
elif 20000<=p<25000:
    print(p,"price before discount")
    p = p - p * 0.4
    print(p, "is the discounted price")
elif 15000<=p<20000:
    print(p,"price before discount")
    p = p - p * 0.3
    print(p, "is the discounted price")
elif 10000<=p<15000:
    print(p,"price before discount")
    p = p - p * 0.2
    print(p, "is the discounted price")
elif 5000<=p<10000:
    print(p,"price before discount")
    p = p - p * 0.1
    print(p, "is the discounted price")
else:
    print("no discount applicable")
    print(p,"payable price")