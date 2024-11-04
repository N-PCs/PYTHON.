ly=int(input("enter the year--> "))
if (ly%4==0 and ly%100!=0 or ly%400==0):
    print(ly,"is leap year")
else:
    print("not leap year")
