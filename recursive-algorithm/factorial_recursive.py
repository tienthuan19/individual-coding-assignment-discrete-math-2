def factorial_recursive(n):
    """
    Computes n! recursively.
    Formula: n! = n * (n-1)! for n > 0, and 0! = 1
    
    Args:
        n: A non-negative integer.
    
    Returns:
        The factorial of n.
    """
    # Base case: 0! is 1
    if n == 0:
        return 1
    
    # Recursive step
    return n * factorial_recursive(n - 1)

# Driver code to test the algorithm
if __name__ == "__main__":
    number = 5
    print(f"The factorial of {number} is: {factorial_recursive(number)}")
    
    # Test with 0
    print(f"The factorial of 0 is: {factorial_recursive(0)}")