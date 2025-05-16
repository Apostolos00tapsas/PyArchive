import matplotlib.pyplot as plt
from math import gcd

"""
Note!! If python2.x verison is used use 
     import fractions
     and replace gcb with factions.gcb

Script Name: fly_straight_dammit.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements the "Fly Straight, Dammit!" sequence (OEIS A133058), a chaotic integer sequence 
    defined by the recursive relation:
        a(1) = a(2) = 1,
        a(n) = a(n-1) + n if gcd(a(n-1), n) = 1,
        a(n) = a(n-1)/gcd(a(n-1), n) otherwise.

    Notable Properties:
        - Exhibits seemingly random behavior despite deterministic definition
        - Contains both bounded and unbounded subsequences
        - Related to prime number distribution and divisibility properties
        - Named after John Conway's exclamation when studying its erratic behavior

    Time Complexity: O(n) for computing the first n terms

Parameters:
    n (int): The number of terms to generate (n >= 1)

Returns:
    numbers: The first n terms of the sequence

Example:
    >>> fly_straight_dammit(10)
    [1, 1, 3, 6, 2, 7, 13, 20, 10, 11]

References:
    - OEIS A133058: https://oeis.org/A133058
    - Numberphile video: https://www.youtube.com/watch?v=pAMgUB51XZA
    - Conway, J.H. (2006) "Some Crazy Sequences"
"""


n = list(range(0, 1000)) #get list of integers (0 - 1000)
numbers = [1, 1] 

for i in n:
    
    if i >= 2:
        if gcd(int(numbers[-1]), i) == 1: #determine if gcd between two numbers is equal to one. 
            a_of_n = numbers[-1] + (i + 1) #create a of n value 
            numbers.append(a_of_n) #append to list 
        else:
        
            GreaterCommonDenom =  gcd(int(numbers[-1]), i) 
            a_of_n = numbers[-1]/GreaterCommonDenom
            numbers.append(int(a_of_n))
    
plt.plot(n, numbers, 'ro') #graph
plt.show()



    
    
    
    

