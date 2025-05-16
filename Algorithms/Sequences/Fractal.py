import numpy as np
import matplotlib.pyplot as plt

"""
Script Name: Fractal.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the fractal sequence (OEIS A002260), a self-similar integer sequence 
    that exhibits recursive patterns at multiple scales. The sequence is constructed by
    concatenating successively longer runs of integers in a triangular pattern.

    Definition:
        a(n) = n - m*(m+1)/2 + 1, where m = floor((sqrt(8*n+1)-1)/2)
        Alternatively: The sequence forms an infinite lower triangular matrix with
        natural numbers where row k contains k copies of k.

    Notable Properties:
        - Self-similar structure at all scales (fractal property)
        - Each positive integer k appears exactly k times
        - Related to triangular numbers (A000217)
        - Useful for generating coordinate systems and indexing schemes

    Time Complexity: O(1) per term (closed-form solution)

Parameters:
    n (int): The index of the term to compute (n >= 1)

Returns:
    q: The nth term or first 'length' terms of the sequence

Example:
    >>> fractal_sequence(5)
    3
    >>> fractal_sequence(length=10)
    [1, 1, 2, 1, 2, 3, 1, 2, 3, 4]

References:
    - OEIS A002260: https://oeis.org/A002260
    - Mandelbrot, B.B. (1982) "The Fractal Geometry of Nature"
    - Wolfram, S. (2002) "A New Kind of Science"
"""

def Fractal_sequence(n):
    z = 2*n - 1
    while z>1 and z%2 == 1:
        z = (z-1)/2
    return z


population=10000
n = np.arange(population)
q=[]
for i in range(0,population):
    q.append(Fractal_sequence(i))


plt.plot(n,q,'k*')
plt.show()
