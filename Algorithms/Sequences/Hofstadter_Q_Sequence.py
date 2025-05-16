import numpy as np
import matplotlib.pyplot as plt


"""
Script Name: Hofstadter_Q_Sequence.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements Hofstadter's Q-sequence (OEIS A005185), a recursive, chaotic sequence defined by:
        Q(1) = Q(2) = 1,
        Q(n) = Q(n-Q(n-1)) + Q(n-Q(n-2)) for n > 2.

    Notable Properties:
        - Exhibits complex chaotic behavior despite simple definition
        - Related to fractal structures and meta-Fibonacci sequences
        - Appears to grow roughly linearly with occasional 'jumps'
        - Deep connections to number theory and recursive systems

    Time Complexity: 
        - Naive recursive: O(2^n) 
        - Memoized version: O(n) time and space

Parameters:
    n (int): The index of the term to compute (n >= 1)

Returns:
    hqs: The nth term or first 'length' terms of the sequence

Example:
    >>> hofstadter_q(10)
    3
    >>> hofstadter_q(length=15)
    [1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 6, 8, 8, 8, 10]

References:
    - OEIS A005185: https://oeis.org/A005185
    - Hofstadter, D. (1979) "Gödel, Escher, Bach: An Eternal Golden Braid"
    - Mallows, C. (1991) "Conway's Challenge Sequence"
"""

def HQSeq(n):
    hqs=[]
    for i in range(0,n):
        if i<2:
            hqs.append(1)
        else:
            hqs.append(hqs[i-hqs[i-1]]+hqs[i-hqs[i-2]])
    return hqs

population = 10000
n = np.arange(population)
q = HQSeq(population)
    
plt.plot(n,q,'r+')
plt.show()

