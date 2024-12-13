"""1. Newton’s Equations of Motion
Question: Write a Python program that takes initial velocity (u), acceleration (a), and
time (t) as inputs and calculates the final velocity (v) and displacement (s) using the
following equations of motion:
								v = u + at
								s = ut +0.5at^2
"""

u=float(input("Enter the initial velocity -> "))
a=float(input("Enter the acceleration -> "))
t=float(input("Enter the time -> "))
#applying the formula v=u +at
v=u+a*t
print("The final velocity is -> ",v)
#applying formula s=ut+0.5at^2
s=u*t+0.5*(a*(t**2))
print("The final displacement is -> ",s)


