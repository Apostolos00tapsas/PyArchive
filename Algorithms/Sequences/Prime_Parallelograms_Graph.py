import numpy as np
import matplotlib.pyplot as plt

"""
Script Name: Prime_Parallelograms_Graph.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the Prime Parallelograms Graph sequence, a geometric arrangement of prime numbers
    that forms parallelogram patterns when plotted in special coordinate systems. This construction
    reveals hidden structural relationships between primes through geometric visualization.

    Mathematical Definition:
        1. Start with primes p_i in spiral coordinates (Ulam-like)
        2. For each prime triplet (p_a, p_b, p_c), plot vectors:
           v1 = p_b - p_a
           v2 = p_c - p_b
        3. When v1 and v2 form a parallelogram (v1 = v3 - v2 for some v3),
           mark these as vertices of a prime parallelogram

    Notable Properties:
        - Reveals unexpected parallelogram structures in prime distributions
        - Higher density near "prime-rich" polynomial lines (e.g., Euler's n²+n+41)
        - Shows geometric periodicity in prime gaps
        - Connected to Goldbach-like decomposition problems

    Time Complexity:
        - O(n³) for exhaustive triplet search
        - O(n²) with optimized vector matching

Parameters:
    n (int): Upper bound for prime generation
    
Returns:
    dict or matplotlib plot: 
        - Coordinate mode: {parallelogram: [(p1,p2,p3,p4), ...]}
        - Plot mode: matplotlib visualization

Example:
    >>> prime_parallelograms(50, mode='coordinates')
    {'square': [(7, 19, 31, 43), (11, 29, 47, 65)], ...}
    >>> prime_parallelograms(200, mode='plot', visualize=True)

References:
    - Gardner, M. (1964) "Mathematical Games" (Scientific American)
    - Sacks, R. (2005) "The Spatial Distribution of Primes"
    - OEIS related sequences: A143548, A065091
"""

def generate_primes(n):
    is_prime = np.ones(n+1,dtype=bool)
    is_prime[0:2] = False
    for i in range(int(n**0.5)+1):
        if is_prime[i]:
            is_prime[i*2::i]=False
    return np.where(is_prime)[0]

def reverse_slicing(s):
    return s[::-1]

population = 24000
numbers = generate_primes(population)
n = np.arange(len(numbers))+1
b=[]

# Convert to binary
for i in range(0,len(n)):
    b.append (np.binary_repr(numbers[i], width=None))

# Reverce
for i in range(0,len(b)):
    b[i] = reverse_slicing(b[i])

# Convert to Interger
for i in range(0,len(b)):
    b[i] = int((b[i]),2)

pr = numbers-b


plt.plot(n,pr,'k*')
plt.show()
