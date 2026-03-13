#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    Calculates the factorial of a given number using recursion.
    The factorial of n is the product of all positive integers less than or equal to n.
    
    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.
    
    Returns:
    int: The factorial of n. Returns 1 if n is 0 (base case).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv))
print(f)
