"""2. Work-Energy Theorem
Question: Design a program to compute the work done on an object given its initial
and final velocities, mass, and the force applied. The work-energy theorem states that
the work done on an object is equal to its change in kinetic energy:

W = ∆KE =0.5m(v^2 − u^2)"""

u=float(input("Enter initial velocity: "))
v=float(input("Enter final velocity: "))
m=float(input("Enter mass: "))

#applying work energy theorem

W=0.5*m*(v**2-u**2)
print("Work done :",W)



