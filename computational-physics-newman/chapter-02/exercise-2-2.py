# A satellite is to be launched into a circular orbit around the Earth so that it orbits the planet once every T seconds.
# The altitude h above the Earth's surface that the satellite must have is defined by the equation:
# h = (GMT^2/(4pi^2))^(1/3)-R
# where G=6.67*10^-11 m^3kg^-1s^-2, M = 5.97*10^24kg and R = 6371km

# a) Write a program that asks the user to enter the desired value of T and then calculates and prints out the correct altitude in meters
# b) Use your program to calculate the altitudes of satellites that orbit the Earth once a day (so-called "geosynchronous" orbit), once every 90 minutes, and once every 45 minutes.
# What do you conclude from the last of these calculations?
# d) Technically a geosynchronous satellite is one that orbits the Earth once per sideral day, which is 23.93 hours and not 24 hours. Why is this?
# And how much difference will it make to the altitude of the satellite?

from math import pi


G = 6.67e-11
M = 5.97e24
R = 6371*1000

T = float(input("Enter the desired value of T, in seconds, for the satellite: "))
h = ((G*M*(T)**2)/(4*pi**2))**(1/3)-R
print(f"The height of the satellite must be: {h}m")
print(f"Or roughly: {h / 1000:.2f} kilometers")

# Result for 45 minutes is negative. It's impossible to have a satellite orbiting the earth with a period of T = 45 minutes.
# Difference between a solar day and a sideral day is, approximately, 80km. This difference is caused by the Earth rotation.
# The time it takes the Earth to complete a full rotation is lesser than the time it takes for the Sun to return to the exact same spot in the sky, due to Earth's rotation.
