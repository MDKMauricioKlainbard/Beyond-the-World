# Write a program to perform the inverse operation to that of Example 2.2. That is, ask the user for the Cartesian
# coordinates x, y of a point in two-dimensional space, and calculate and print the corresponding polar coordinates,
# with the angle theta given in degrees.

from math import atan, pi, sqrt


x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))
r = sqrt(x**2+y**2)
theta = 0.0

if x == 0:
    if y > 0:
        theta = 90
    elif y < 0:
        theta = 270
    else:
        theta = 0
elif x < 0:
    theta = 180 + atan(y/x) * 180/pi
else:
    theta = atan(y/x)*180/pi

print(f"Polar coordinates: ({r:.2f}, {theta:.2f})")