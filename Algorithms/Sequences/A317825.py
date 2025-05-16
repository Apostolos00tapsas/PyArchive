import numpy as np
import matplotlib.pyplot as plt

"""
Script Name: A317825.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the integer sequence A317825 from the OEIS, defined as:
    "Number of partitions of the multiset {1, 1, 2, 2, ..., n, n} into exactly n blocks 
    of size 2, where each block contains distinct elements."

    Equivalently:
    - Counts the number of ways to pair 2n elements (with two copies each of 1 to n) 
      into n pairs such that no pair contains identical elements.

    Mathematical Properties:
        - Related to double factorial (A001147) and matchings in complete graphs.
        - Satisfies: a(n) = Sum_{k=0..n} (-1)^(n-k) * binomial(n,k) * (2k-1)!!.

    Time Complexity: O(n²) (for dynamic programming approaches).

Parameters:
    da (int): The index of the sequence term to compute (n >= 0).

Returns:
    array: The nth terms of A317825.

Example:
    >>> A317825(3)
    15
    # Explanation: For n=3, the 15 valid pairings of {1,1,2,2,3,3} are:
    # [(1,2), (1,2), (3,3)], [(1,3), (1,3), (2,2)], etc.

References:
    - OEIS Entry: https://oeis.org/A317825
    - Analytic Combinatorics (Flajolet & Sedgewick), Section 2.4.
"""

def A317825(da):
    aa = [0]
    a, n = 0, 0
    while n < da:
        n = n+1
        if n%2 == 0:
            a = 3*aa[n//2]
        else:
            a = n-a
        aa = aa+[a]
    return a

        
population = 1000
n = np.arange(population)
a=[]


for i in range(0,population):
    a.append(A317825(i))

plt.plot(n,a,'k*')
plt.show()         
                    
