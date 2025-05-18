"""
Script Name: Hanoi.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements of Hanoi problem.

Parameters:
    n (int): The number of swarm.
    f (int):
    h (int):
    t (int):
    
Returns:
    

Example:
    hanoi(5,3,1,1)
"""


def move(f,t):
    print ("Move disc from {} to {}".format(f,t))

    
def hanoi(n,f,h,t):
    if n<=0:
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)


hanoi(5,3,1,1)

        

    
