import numpy as np
import matplotlib.pyplot as plt

"""
Script Name: forest_fire.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the "Forest Fire" sequence (OEIS A229037), a self-referential sequence 
    where each term describes the distance back to the previous occurrence of its value.
    The sequence 'burns' like a forest fire, with numbers spreading until encountering
    their previous occurrence.

    Definition:
        a(1) = a(2) = 1,
        For n > 2:
        a(n) = number of steps back to the most recent a(n-1) if it exists,
        otherwise a(n) = a(n-1) + 1 (the 'fire spreads').

    Notable Properties:
        - Exhibits fractal-like behavior with 'burning' and 'growth' phases
        - Contains both predictable linear growth and chaotic jumps
        - Related to sequence memory and self-describing sequences
        - Visualizations resemble forest fire patterns

    Time Complexity: O(n²) worst case (due to backward searching)

Parameters:
    n (int): The number of terms to generate (n >= 1)

Returns:
    forest: The first n terms of the sequence

Example:
    >>> forest_fire(10)
    [1, 1, 2, 1, 2, 3, 1, 3, 2, 4]

References:
    - OEIS A229037: https://oeis.org/A229037
    - Numberphile video: https://www.youtube.com/watch?v=V4oRHv-SvwE
    - Sloane, N.J.A. (2013) "My Favorite Integer Sequences"
"""

def forest_fire_sequence(n):
    forest = []
    for n in range(n):
        i, j, b = 1, 1, set()
        while n-2*i >= 0:
            b.add(2*forest[n-i]-forest[n-2*i])
            i += 1
            while j in b:
                b.remove(j)
                j += 1
        forest.append(j)
    return forest


population = 10000
n = np.arange(population)
f=forest_fire_sequence(population)


plt.plot(n,f,'r+')
plt.show()
