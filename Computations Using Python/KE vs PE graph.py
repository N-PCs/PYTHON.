import numpy as np
import matplotlib.pyplot as plt

# Define constants
m = 1.0  # mass in kg
w = 1.0  # angular frequency in rad/s
A = 1.0  # amplitude in meters

# Generate x values for plotting
x = np.linspace(-A, A, 100)  # from -A to +A

# Calculate potential and kinetic energy
PE = 0.5 * m * w**2 * x**2  # Potential Energy
KE = 0.5 * m * w**2 * (A**2 - x**2)  # Kinetic Energy

# Total Energy (constant)
E = 0.5 * m * w**2 * A**2

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, PE, label='Potential Energy', color='red')
plt.plot(x, KE, label='Kinetic Energy', color='blue')
plt.axhline(y=E, color='green', linestyle='--', label='Total Energy')

# Setting up the plot
plt.xlabel('Displacement (m)')
plt.ylabel('Energy (J)')
plt.title('Energy in Simple Harmonic Motion')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
