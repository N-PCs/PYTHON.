name="Neel"
number=len(name)*3
print("Hello {}, your lucky number is {}".format(name,number))

#This is the best way to print a string.
#Curly brackets placeholder show where the variables should be written.
#We then pass the variables as a parameter to the format method.

print("Your lucky number is {number}, {name}. ".format(name=name,number=len(name)*3))
#Here we are defining the conditions inside parentheses of .format

print("Your lucky number is {number}, {name}. ".format(name="N_PCs",number=len(name)*2))
print("\n")

#Q2
''' Modify the student_grade function using the format method, 
	so that it returns the phrase "X received Y% on the exam". 
	For example, student_grade("Reed", 80) should return 
	"Reed received 80% on the exam".
'''
#SOLUTION

def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format(name=name,grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

'''OUTPUT:
	Reed received 80% on the exam
	Paige received 92% on the exam
	Jesse received 85% on the exam
'''
print("\n")
price= 7.5
with_tax=price*1.09
print(price,with_tax)
print("Base price= ${:.2f}. With Tax: ${:.2f}".format(price,with_tax))
#Using {:.2f} we can print the values of variables upto two decimal places.
#Used format the values given by user.
print("\n")

#Q3
'''Using formatting function write a program 
	to convert fahrenheit to celsius program'''
#SOLUTION

def fahrenheit_to_celsius(x):
	return (x - 32) * 5 / 9

for x in range(-100,101,10):
	print(x,"F => ","{:.3f} C".format((x - 32) * 5 / 9))
#Will print temperatures upto 3 decimal places.
print('\n')

#Eg:
#  - ":10" makes the output 10 characters wide.
#  - "," inserts thousands separators between groups of digits.
#  - ".2" limits the output to two digits after the decimal.
#  - "f" tells Python to expect a floating-point number.
subtotal=float(input("Enter subtotal: "))
tax_amt=float(input("Enter tax amount: "))
total=subtotal+tax_amt
print("Subtotal:  ${:10,.2f}".format(subtotal))
print("Sales Tax: ${:10,.2f}".format(tax_amt))
print("Total: ${:10,.2f}".format(total))










