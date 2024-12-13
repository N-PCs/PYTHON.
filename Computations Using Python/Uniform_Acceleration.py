def distance_uniform_acceleration(u, a, t):            #uniform
	return u * t + 0.5 * a * t ** 2
# Example usage
initial_velocity = 5  # m/s
acceleration = 2  # m/s^2
time = 10  # seconds
distance = distance_uniform_acceleration(initial_velocity, acceleration, time)
print(f"Distance traveled under uniform acceleration: {distance} meters")

def distance_non_uniform_acceleration(u, k, time_intervals):           #non-uniform
	distances = []
	total_distance = 0
	for i in range(1, len(time_intervals)):
		t1 = time_intervals[i - 1]
		t2 = time_intervals[i]
		dt = t2 - t1
		avg_acceleration = k * (t1 + t2) / 2
		v = u + avg_acceleration * t1
		s = v * dt + 0.5 * avg_acceleration * dt ** 2
		total_distance += s
		distances.append(total_distance)

	return distances
initial_velocity = 5  # m/s
k = 1  # Constant for acceleration function
time_intervals = [i * 0.1 for i in range(0, 101)]  # Time intervals from 0 to 10 seconds
distances = distance_non_uniform_acceleration(initial_velocity, k, time_intervals)
# Output results
print("Time (s)    Distance (m)")
for t, d in zip(time_intervals, distances):
	print(f"{t:.2f}         {d:.2f}")
	

