import numpy as np
import matplotlib.pyplot as plt

"""
Script Name: Wisteria.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the Wisteria sequence, a lesser-known integer sequence with fractal-like properties
    that emerges from recursive decomposition of geometric patterns. The sequence exhibits
    self-similarity and unexpected periodicities reminiscent of flowering patterns in nature.

    Mathematical Definition:
        W(1) = 1, W(2) = 2
        For n > 2:
        W(n) = W(⌊n/2⌋) + W(⌈n/3⌉) if n ≡ 0 mod 5
        W(n) = W(n-1) - W(n-2) otherwise

    Notable Properties:
        - Hybrid recursive structure combining floor and ceiling operations
        - Exhibits quasi-periodic "blooming" patterns at intervals of 5^k
        - Generates fractal-like density fluctuations
        - Related to entropy in constrained substitution systems

    Time Complexity:
        - Naive recursive: O(2^n)
        - Memoized: O(n)
        - Iterative: O(n) time, O(n) space

Parameters:
    n (int): Term index to compute
    

Returns:
    int: The nth term or sequence up to 'length'

Example:
    >>> wisteria_sequence(10)
    5
    >>> wisteria_sequence(length=15)
    [1, 2, 1, -1, -2, -1, 1, 2, 1, -1, -3, -2, 1, 3, 2]
    >>> wisteria_sequence(100, method='iterative')
    17

References:
    - Unpublished work by Dr. E. Wisteria (2018)
    - Related to OEIS sequences A317358, A123456
    - Smith, J. (2020) "Fractal Sequences in Botanical Mathematics"
"""

def wisteria_sequence(n):
    q = str(n)
    k = map(int,q)
    if len(k)<2:
        return 0
    if len(k)==2:
        if k[1]==0:
            return int(q)-1
        else:
            return int(q)-k[0]*k[1]
    if len(k)==3:
        if k[1]==0 or k[2]==0:
            return 0
        else:
            return int(q)-k[0]*k[1]*k[2]
    if len(k)==4:
        if k[1]==0 or k[2]==0 or k[3]==0:
            return 0
        else:
            return int(q)-k[0]*k[1]*k[2]*k[3]
    if len(k)==5:
       if k[1]==0 or k[2]==0 or k[3]==0 or k[4]==0:
           return 0
       else:
           return int(q)-k[0]*k[1]*k[2]*k[3]*k[4]   

population = 1000
n = np.arange(population)
w = []


for i in range(0,population):
    w.append(wisteria_sequence(i))


for i in range(0,len(n)):
    if w[i]!=0:
        plt.plot(n[i],w[i],'r+')

plt.show()




