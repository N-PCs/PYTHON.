import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.8  # Acceleration due to gravity (m/s^2)
v0 = float(input("Enter the initial velocity >> "))  # Initial velocity (m/s)
angle = float(input("Enter the launch angle >> "))  # Launch angle (degrees)

# Convert angle to radians
angle_rad = np.radians(angle)

# Time of flight
t_flight = 2 * v0 * np.sin(angle_rad) / g

# Time array
t = np.linspace(0, t_flight, num=500)

# Equations of motion
x = v0 * np.cos(angle_rad) * t
y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Trajectory of the projectile', color='b')
plt.title('\n Projectile Motion: Vertical Distance vs. Horizontal Distance')

# Add description of initial values
description = f'Initial Velocity: {v0:.2f} m/s\nLaunch Angle: {angle:.2f} degrees\nGravity: {g} m/s^2'

# Annotate initial values
plt.annotate(description, xy=(0.5, 1.1), xycoords='axes fraction',
             ha='left', va='center_baseline', fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.grid(True)
plt.legend()
plt.xlim(0, np.max(x))  # Ensure the plot shows from 0 to max range of projectile
plt.ylim(0, np.max(y))  # Ensure the plot shows from 0 to max height of projectile
plt.show()