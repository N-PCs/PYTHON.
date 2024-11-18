a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
s = min(a, b)
n = max(a, b)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = []
for i in range(s, n + 1):
    if is_prime(i):
        prime_numbers.append(i)

print("Prime numbers in the range:", prime_numbers)






