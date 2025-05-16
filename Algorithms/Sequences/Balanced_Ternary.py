import numpy as np
import matplotlib.pyplot as plt

"""
Script Name: balanced_ternary.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the balanced ternary numeral system (base-3 with digits {-1, 0, 1}), 
    represented by the OEIS sequence A117966. Each integer maps uniquely to a balanced 
    ternary string, enabling efficient signed arithmetic without a separate sign bit.

    Key Properties:
        - Digit Set: Uses {-1, 0, 1}, often denoted as {-, 0, +}.
        - Uniqueness: Every integer has a unique representation.
        - No Sign Bit: The sign is encoded in the digits themselves.
        - Applications: Used in fault-tolerant computing and ternary logic circuits.

    Mathematical Definition:
        For a balanced ternary string d_k...d_0, its decimal value is:
            Σ_{i=0}^k (d_i * 3^i), where d_i ∈ {-1, 0, 1}.

    Time Complexity:
        - Conversion to balanced ternary: O(log_3 n).
        - Arithmetic operations: Typically O(n) for n-digit numbers.

Parameters:
    population (int): The integer to convert to balanced ternary (can be positive, negative, or zero).

Returns:
    list: The balanced ternary representation (e.g., "+0-" or [1, 0, -1]).

Example:
    >>> to_balanced_ternary(5)
    "+--"  # Equivalent to 1*3^2 + (-1)*3^1 + (-1)*3^0 = 9 - 3 - 1 = 5
    >>> to_balanced_ternary(-7)
    "-0+"  # -1*3^2 + 0*3^1 + 1*3^0 = -9 + 0 + 1 = -8

References:
    - OEIS A117966: https://oeis.org/A117966
    - Knuth, D.E. "The Art of Computer Programming", Vol. 2, Section 4.1.
    - Wikipedia: https://en.wikipedia.org/wiki/Balanced_ternary
"""

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

population = 1050

n = np.arange(population)
q=[]
for i in range(0,population):
    z = ternary(i)
    k=map(int,z)
    for i in range(0,len(k)):
        if k[i]==2:
            k[i]=-1
    if len(k)<2:
        q.append(k[0])
    elif len(k)==2:
        q.append(k[0]*3**1   +    k[1])
    elif len(k)==3:
        q.append(k[0]*3**2  +  k[1]*3**1 + k[2])
    elif len(k)==4:
        q.append(k[0]*3**3* +  k[1]*3**2 + k[2]*3**1 + k[3])
    elif len(k)==5:
        q.append(k[0]*3**4* +  k[1]*3**3 + k[2]*3**2 + k[3]*3**1 + k[4])
    elif len(k)==6:
        q.append(k[0]*3**5* +  k[1]*3**4 + k[2]*3**3 + k[3]*3**2 + k[4]*3**1 + k[5])
    elif len(k)==7:
        q.append(k[0]*3**6* +  k[1]*3**5 + k[2]*3**4 + k[3]*3**3 + k[4]*3**2 + k[5]*3**1 + k[6])
    elif len(k)==8:
        q.append(k[0]*3**7* +  k[1]*3**6 + k[2]*3**5 + k[3]*3**4 + k[4]*3**3 + k[5]*3**2 + k[6]*3**1 + k[7])
    elif len(k)==9:
        q.append(k[0]*3**8* +  k[1]*3**7 + k[2]*3**6 + k[3]*3**5 + k[4]*3**4 + k[5]*3**3 + k[6]*3**2 + k[7]*3**1+k[8])

plt.plot(n,q,'k*')
plt.show()

