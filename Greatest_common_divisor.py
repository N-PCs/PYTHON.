# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Finding the smaller number to iterate over
smaller = min(num1, num2)

# Initializing GCD to 1
gcd = 1

# Iterating from 1 to the smaller number
for i in range(1, smaller + 1):
    if (num1 % i == 0) and (num2 % i == 0):
        gcd = i

# Printing the GCD
print("GCD of", num1, "and", num2, "is", gcd)


# ------------------------------------------------------------

# Another method (from SamXop123)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculating GCD using Euclidean algorithm
def calculate_gcd(a, b):
    while b != 0:
        temp = b          
        b = a % b         
        a = temp         
    return a

gcd = calculate_gcd(num1, num2)
print(f"GCD of {num1} and {num2} is {gcd}")

