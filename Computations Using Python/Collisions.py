"""7. Collision of Particles
Question: Implement an algorithm that simulates an elastic collision between two particles
in one dimension. Given the masses and velocities of two particles, calculate their velocities after the collision.
Use the formula for elastic collisions in one dimension:
"""
def elastic_collision(m1, v1, m2, v2):

	v1_final = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
	v2_final = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
	return v1_final, v2_final

m1 =float(input("Mass of particle 1: "))
v1 = float(input("Velocity of particle 1: "))
m2 = float(input("Mass of particle 2: "))
v2 = float(input("Velocity of particle 2: "))

v1_final, v2_final = elastic_collision(m1, v1, m2, v2)
print(f"Final velocity of particle 1: {v1_final:.2f} m/s")
print(f"Final velocity of particle 2: {v2_final:.2f} m/s")
