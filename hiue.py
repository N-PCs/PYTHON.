m=100
while m in range(100,1000):
    s=0
    a=m
    if m>0:
        p=m%10
        m=m//10
        s=s*10+p
        if a==s:
            print(m)
