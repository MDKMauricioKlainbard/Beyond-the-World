# Exercise 2.4: A spaceship travels from Earth in a straight line at relativistic 
# speed v to another planet x light years away. Write a program to ask the user 
# for the value of x and the speed v as a fraction of the speed of light c, then 
# print out the time in years that the spaceship takes to reach its destination 
# (a) in the rest frame of an observer on Earth and (b) as perceived by a 
# passenger on board the ship. Use your program to calculate the answers for a 
# planet 10 light years away with v = 0.99c.

from math import sqrt

c = 2.99e8 # Speed of light measured in m/s
b = float(input("Enter speed of the spaceship as a fraction of the speed of light c (0-1.0): "))
x = float(input("Enter distance in light years to destination: "))
v = b*c
t_earth = x / b # Earth's frame
t_passenger = t_earth*sqrt(1-b**2) # Passenger's frame

print(f"Time in years to reach destination (Earth's frame): {t_earth:.2f}")
print(f"Time in years to reach destination (Passenger's frame): {t_passenger:.2f}")