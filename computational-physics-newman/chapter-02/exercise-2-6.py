"""
Exercise 2.6: Planetary orbits

The orbit in space of one body around another, such as a planet around the Sun, 
need not be circular. In general it takes the form of an ellipse, with the body 
sometimes closer in and sometimes further out. If you are given the distance l1 
of closest approach that a planet makes to the Sun, also called its perihelion, 
and its linear velocity v1 at perihelion, then any other property of the orbit 
can be calculated from these two as follows.

a) Kepler's second law tells us that the distance l2 and velocity v2 of the 
   planet at its most distant point, or aphelion, satisfy l2*v2 = l1*v1. At the 
   same time the total energy, kinetic plus gravitational, of a planet with 
   velocity v and distance r from the Sun is given by
   
     E = (1/2)*m*v^2 - G*(m*M)/r ,
     
   where m is the planet's mass, M = 1.9891 x 10^30 kg is the mass of the Sun, 
   and G = 6.6738 x 10^-11 m^3*kg^-1*s^-2 is Newton's gravitational constant. 
   Given that energy must be conserved, show that v2 is the smaller root of the 
   quadratic equation:
   
     v2^2 - (2*G*M / (v1*l1))*v2 - [v1^2 - (2*G*M / l1)] = 0.
     
   Once we have v2 we can calculate l2 using the relation l2 = l1*v1 / v2.

b) Given the values of v1, l1, and l2, other parameters of the orbit are given 
   by simple formulas can that be derived from Kepler's laws and the fact that 
   the orbit is an ellipse:
   
     Semi-major axis:      a = (1/2) * (l1 + l2),
     Semi-minor axis:      b = sqrt(l1 * l2),
     Orbital period:       T = (2 * pi * a * b) / (l1 * v1),
     Orbital eccentricity: e = (l2 - l1) / (l2 + l1).

   Write a program that asks the user to enter the distance to the Sun and 
   velocity at perihelion, then calculates and prints the quantities l2, v2, T, and e.

c) Test your program by having it calculate the properties of the orbits of the 
   Earth (for which l1 = 1.4710 x 10^11 m and v1 = 3.0287 x 10^4 m/s) and Halley's 
   comet (l1 = 8.7830 x 10^10 m and v1 = 5.4529 x 10^4 m/s). Among other things, 
   you should find that the orbital period of the Earth is one year and that of 
   Halley's comet is about 76 years.
"""

from math import pi, sqrt


M = 1.9891e30 # Mass of the sun (kg)
G = 6.6738e-11 # Newton's gravitational constant (m^3kg^-1s^-2)

v1_earth = 3.0287e4
l1_earth = 1.4710e11

v1_halley = 5.4529e4
l1_halley = 8.7830e10
# Solve the quadratic formula for the smaller root:
# a = 1 for both bodies
b_earth = -2*G*M/(v1_earth*l1_earth)
c_earth = -(v1_earth**2 - 2*G*M/l1_earth)

b_halley = -2*G*M/(v1_halley*l1_halley)
c_halley = -(v1_halley**2 - 2*G*M/l1_halley)

v2_earth = (-b_earth-sqrt(b_earth**2-4*c_earth))/2
v2_halley = (-b_halley-sqrt(b_halley**2-4*c_halley))/2

l2_earth = (l1_earth*v1_earth)/v2_earth
l2_halley = (l1_halley*v1_halley)/v2_halley

major_axis_earth = (l1_earth+l2_earth)/2
major_axis_halley = (l1_halley+l2_halley)/2

minor_axis_earth = sqrt(l1_earth*l2_earth)
minor_axis_halley = sqrt(l1_halley*l2_halley)

T_earth = (2*pi*major_axis_earth*minor_axis_earth)/(l1_earth*v1_earth)
T_halley = (2*pi*major_axis_halley*minor_axis_halley)/(l1_halley*v1_halley)

e_earth = (l2_earth-l1_earth)/(l2_earth+l1_earth)
e_halley = (l2_halley-l1_halley)/(l2_halley+l1_halley)

conversion_seconds_to_years = 1/31536000
conversion_meters_to_kilometers = 1/1000

print("Earth data")
print(f"Orbital period in years: {T_earth*conversion_seconds_to_years}")
print(f"Velocity at aphelion: {v2_earth:.2f}m/s")
print(f"Distance at the sun in aphelion: {l2_earth*conversion_meters_to_kilometers:.2f}km")
print(f"Excentricity: {e_earth:.4f}")
print("---")
print("Halley's comet data")
print(f"Orbital period in years: {T_halley*conversion_seconds_to_years}")
print(f"Velocity at aphelion: {v2_halley:.2f}m/s")
print(f"Distance at the sun in aphelion: {l2_halley*conversion_meters_to_kilometers:.2f}km")
print(f"Excentricity: {e_halley:.4f}")