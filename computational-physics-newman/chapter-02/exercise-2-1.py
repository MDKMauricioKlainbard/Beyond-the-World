# A ball is dropped from a tower of height h with initial velocity zero. Write a program that asks the user to enter
# the height in meters of the tower and then calculates and prints the time the ball takes until it hits the ground, ignoring
# air resistance. Use your program to calculate the time for a ball dropped from a 100m high tower.

g = 9.81
h = float(input("Enter the height in meters of the tower: "))
t = (2*h/g)**0.5
print(f"Time the ball takes to hit the ground: {t}")    