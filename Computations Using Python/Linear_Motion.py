""""4. Linear Motion
Question: Write a program to simulate the motion of an object with constant velocity.
Given the initial position and velocity, calculate the position of the object at various time
intervals."""

def calculate_positions(initial_position, velocity, time_intervals):
    positions = []
    for time in time_intervals:
        position = initial_position + (velocity * time)
        positions.append((time, position))
    return positions

initial_position = float(input("Enter the initial position (in meters): "))
velocity = float(input("Enter the constant velocity (in meters/second): "))
time_intervals = [0, 1, 2, 3, 4, 5]

positions = calculate_positions(initial_position, velocity, time_intervals)

print("Time (s)    Position (m)")
for time, position in positions:
    print(f"{time:9}    {position:10.2f}")


