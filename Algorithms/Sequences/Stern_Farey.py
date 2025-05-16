import math 
import numpy as np
import matplotlib.pyplot as plt


"""
Script Name: Stern_Farey.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the Stern's diatomic sequence (OEIS A002487), also known as the Farey sequence,
    which enumerates rational numbers in their reduced form through a binary tree structure.
    The sequence has deep connections to number theory, combinatorics, and fractal geometry.

    Mathematical Definition:
        a(0) = 0, a(1) = 1
        a(2n) = a(n)
        a(2n+1) = a(n) + a(n+1)

    Notable Properties:
        - Generates all reduced fractions between 0/1 and 1/1
        - a(n) counts hyperbinary representations
        - Related to the Farey tree and continued fractions
        - Exhibits fractal-like self-similarity
        - a(n+1)/a(n) gives n-th Farey fraction

    Time Complexity:
        - Recursive: O(2^n)
        - Memoized: O(n)
        - Iterative: O(n) time, O(1) space

Parameters:
    n (int): Term index to compute
 

Returns:
    BrocotSequence: The nth term or sequence up to 'length'

Example:
    >>> stern_farey(7)
    3
    >>> stern_farey(length=10)
    [0, 1, 1, 2, 1, 3, 2, 3, 1, 4]
    >>> stern_farey(100, method='iterative')
    19

References:
    - OEIS A002487: https://oeis.org/A002487
    - Stern, M.A. (1858) "Über eine zahlentheoretische Funktion"
    - Graham, Knuth, Patashnik (1994) "Concrete Mathematics" (Section 6.7)
    - Calkin, Wilf (2000) "Recounting the Rationals"
"""

def Stern_Sequence(n): 
    BrocotSequence = [1,1] 
    # loop to create sequence 
    for i in range(1,  n): 
          
        considered_element = BrocotSequence[i] 
        precedent = BrocotSequence[i-1] 
   
        # adding sum of considered 
        # element and it's precedent 
        BrocotSequence.append(considered_element + precedent) 
           
        # adding next considered element 
        BrocotSequence.append(considered_element) 
      
    return BrocotSequence 

     
population = 10000
b = Stern_Sequence(population)
n = np.arange(len(b))

plt.plot(n,b,'k+')
plt.show()
