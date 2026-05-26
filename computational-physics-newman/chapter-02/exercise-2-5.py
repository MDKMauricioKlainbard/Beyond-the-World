"""
Exercise 2.5: Quantum potential step

A well-known quantum mechanics problem involves a particle of mass m that encoun-
ters a one-dimensional potential step, like this:


         |            ....... E
      R  |     T      _______ V
    <--  |   -->     |
 incoming|           |
    -->  |           |
_________|___________|___________
         0

The particle with initial kinetic energy E and wavevector k1 = sqrt(2mE)/hbar 
enters from the left and encounters a sudden jump in potential energy of height 
V at position x = 0. By solving the Schrödinger equation, one can show that 
when E > V the particle may either:
  (a) pass the step, in which case it has a lower kinetic energy of E - V on 
      the other side and a correspondingly smaller wavevector of 
      k2 = sqrt(2m(E - V))/hbar, or 
  (b) it may be reflected, keeping all of its kinetic energy and an unchanged 
      wavevector but moving in the opposite direction. 

The probabilities T and R for transmission and reflection are given by:
  T = (4 * k1 * k2) / (k1 + k2)^2
  R = ((k1 - k2) / (k1 + k2))^2

Suppose we have a particle with mass equal to the electron mass 
m = 9.11 x 10^-31 kg and energy 10 eV encountering a potential step of height 9 eV. 
Write a Python program to compute and print out the transmission and reflection 
probabilities using the formulas above.
"""

from math import sqrt


m = 9.11e-31 # Electron mass
E = 10 # Initial electron's kinetic energy measured in eV.
V = 9 # Potential step measured in eV.
h = 6.63e-34 # Planck's constant in m^2kg/s
k1 = sqrt(2*m*E)/h
k2 = sqrt(2*m*(E-V))/h
T = (4*k1*k2)/(k1+k2)**2
R = ((k1-k2)/(k1+k2))**2

print(f"Probability of transmission: {T:.4f}")
print(f"Probability of reflection: {R:.4f}")
print(f"Total probability: {T+R:.4f}") # Should always equal 1.0