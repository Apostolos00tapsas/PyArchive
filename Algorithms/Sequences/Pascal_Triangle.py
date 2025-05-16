import numpy as np
import matplotlib.pyplot as plt


  # Pascal's Triangle
  
  #n\k 0   1   2   3   4   5   6   7   8   9  10  11...
  # 0   1
  # 1   1   1
  # 2   1   2   1
  # 3   1   3   3   1
  # 4   1   4   6   4   1
  # 5   1   5  10  10   5   1
  # 6   1   6  15  20  15   6   1
  # 7   1   7  21  35  35  21   7   1
  # 8   1   8  28  56  70  56  28   8   1
  # 9   1   9  36  84 126 126  84  36   9   1
  # 10   1  10  45 120 210 252 210 120  45  10   1
  # 11   1  11  55 165 330 462 462 330 165  55  11   1

"""
Script Name: Pascal_Triangle.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements Pascal's Triangle (OEIS A007318), a triangular array of binomial coefficients
    where each number is the sum of the two directly above it. The triangle demonstrates
    fundamental combinatorial mathematics and appears in probability, algebra, and number theory.

    Mathematical Definition:
        C(n, k) = n!/(k!(n-k)!)  for 0 ≤ k ≤ n
        Recursive relation: C(n, k) = C(n-1, k-1) + C(n-1, k)

    Notable Properties:
        - Symmetry: C(n, k) = C(n, n-k)
        - Diagonals correspond to figurate numbers
        - Sum of nth row = 2^n
        - Fibonacci numbers appear in shallow diagonals

    Time Complexity:
        - Direct computation: O(n^2) for n rows
        - Single coefficient: O(k) time, O(1) space

Parameters:
    n (int): Row index (0-based)
    k (int, optional): Column index (0-based)    

Returns:
    res: Requested row, full triangle, or specific coefficient

Example:
    >>> pascal_triangle(n=4, mode='row')
    [1, 4, 6, 4, 1]
    >>> pascal_triangle(k=3, mode='coefficient', n=5)
    10
    >>> pascal_triangle(rows=3)
    [[1], [1, 1], [1, 2, 1]]

References:
    - OEIS A007318: https://oeis.org/A007318
    - Graham, Knuth, Patashnik (1994) "Concrete Mathematics"
    - Pascal (1654) "Traité du Triangle Arithmétique"
"""



def binomialCoeff(n, k) : 
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1) 
      
    return res


population = 100
n = np.arange(population)
q = []
for i in range (0,population):
        q.append(binomialCoeff(population,i))

plt.plot(n,q,'r+')
plt.show()



