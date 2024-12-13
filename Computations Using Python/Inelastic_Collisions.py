"""
9. Inelastic Collision Question: Write a program to simulate a perfectly inelastic
collision between two par- ticles in 1D. In this case, both particles stick together
after the collision, and momentum is conserved.
The final velocity can be calculated using the formula: vf = (m1v1 + m2v2)/ (m1 + m2)
"""


def inelastic_collision(m1, v1, m2, v2):
	vf = (m1 * v1 + m2 * v2) / (m1 + m2)
	return vf


# Example usage
m1 = float(input("Enter mass of 1 : "))  # Mass of particle 1 in kg
v1 = float(input("Enter velocity of 1 : ")) # Initial velocity of particle 1 in m/s
m2 = float(input("Enter mass of  : "))  # Mass of particle 2 in kg
v2 = float(input("Enter velocity of  : ")) # Initial velocity of particle 2 in m/s

final_velocity = inelastic_collision(m1, v1, m2, v2)
print(f"Final velocity after collision: {final_velocity:.2f} m/s")
