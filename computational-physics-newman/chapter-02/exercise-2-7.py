"""
Exercise 2.7: Catalan numbers

The Catalan numbers C_n are a sequence of integers 1, 1, 2, 5, 14, 42, 132... that play
an important role in quantum mechanics and the theory of disordered systems. (They
were central to Eugene Wigner's proof of the so-called semicircle law.) They are given by

     C_0 = 1,   C_{n+1} = ((4n + 2) / (n + 2)) * C_n

Write a program that prints in increasing order all Catalan numbers less than or equal
to one billion.
"""

limit = 1_000_000_000
cn = 1
n = 0

while cn <= limit:
    print(cn)
    cn = ((4*n+2) * cn) // (n+2)
    n += 1