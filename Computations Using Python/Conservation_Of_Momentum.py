"""10. Conservation Laws Question: Create a program to simulate the
conservation of momentum in a closed system with multiple particles.
Given the masses and initial velocities of several particles,
calculate their final velocities assuming no external forces act on the system.
"""

def conservation_of_momentum(masses, velocities):
	# Calculate initial total momentum
	total_momentum = sum(m * v for m, v in zip(masses, velocities))

	# Calculate total mass
	total_mass = sum(masses)

	# Calculate final velocity for each particle (assuming momentum is distributed based on mass)
	final_velocities = [total_momentum / total_mass for _ in masses]

	return final_velocities


# Example usage
masses = [2.0, 3.0, 1.5]  # Masses of the particles in kg
velocities = [3.0, -1.0, 2.0]  # Initial velocities of the particles in m/s

final_velocities = conservation_of_momentum(masses, velocities)
print("Final velocities of the particles:\n", final_velocities)
