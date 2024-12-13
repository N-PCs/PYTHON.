import math
def projectile_motion(v0, theta, time_intervals):
	g = 9.81  # Acceleration due to gravity in m/s^2
	theta_rad = math.radians(theta)  # Convert angle to radians
	positions = []

	for t in time_intervals:
		x = v0 * math.cos(theta_rad) * t
		y = v0 * math.sin(theta_rad) * t - 0.5 * g * t** 2

		# Stop calculation when the projectile hits the ground
		if y < 0:
			break

		positions.append((t, x, y))

	return positions

initial_velocity = float(input("Enter the initial velocity (in m/s): "))
launch_angle = float(input("Enter the launch angle (in degrees): "))
time_intervals = [i * 0.1 for i in range(0, 101)]  # Time intervals in seconds (0 to 10 seconds, step 0.1)

# Calculate positions at various time intervals
positions = projectile_motion(initial_velocity, launch_angle, time_intervals)

# Output the results
print("Time (s)    X Position (m)    Y Position (m)")
for t, x, y in positions:
	print(f"{t:9.2f}    {x:15.2f}    {y:15.2f}")


