"""3. Conservative Forces
Question: Write a function to compute the potential energy stored in a spring using
Hooke’s Law. The formula for the potential energy stored in a spring is:
				U=0.5kx^2
Where k is the spring constant, and x is the displacement from equilibrium.
"""
def potential_energy(k, x):
    U = 0.5 * k * x**2
    return U

k = float(input("Enter the spring constant (k): "))
x = float(input("Enter the displacement from equilibrium (x): "))

# Compute the potential energy
E = potential_energy(k, x)
print("The potential energy stored in the spring is ", E ," joules.")
