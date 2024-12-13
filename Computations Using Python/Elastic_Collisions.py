"""8. Elastic Collision
Question: Extend the previous problem by simulating a 2D elastic collision between
two particles. Implement the following steps:
1. Decompose the velocities into components along the normal and tangential directions.
2. Apply the 2D elastic collision equations to update the velocities in each direction.
"""
import numpy as np
def elastic_collision_2d(m1, v1, r1, m2, v2, r2):
	r_rel = r1 - r2
	n = r_rel / np.linalg.norm(r_rel)
	v1n = np.dot(v1, n)
	v2n = np.dot(v2, n)
	v1t = v1 - v1n * n
	v2t = v2 - v2n * n
	v1n_prime = (v1n * (m1 - m2) + 2 * m2 * v2n) / (m1 + m2)
	v2n_prime = (v2n * (m2 - m1) + 2 * m1 * v1n) / (m1 + m2)
	v1_prime = v1n_prime * n + v1t
	v2_prime = v2n_prime * n + v2t
	return v1_prime, v2_prime

m1 = 2.0  # Mass of particle 1 in kg
v1 = np.array([3.0, 1.0])  # Initial velocity of particle 1 in m/s
r1 = np.array([0.0, 0.0])  # Position of particle 1

m2 = 3.0  # Mass of particle 2 in kg
v2 = np.array([-1.0, 2.0])  # Initial velocity of particle 2 in m/s
r2 = np.array([1.0, 1.0])  # Position of particle 2

v1_prime, v2_prime = elastic_collision_2d(m1, v1, r1, m2, v2, r2)
print(f"Final velocity of particle 1: {v1_prime}")
print(f"Final velocity of particle 2: {v2_prime}")
