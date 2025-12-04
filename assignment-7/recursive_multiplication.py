def recursive_multiplication(n, x):
    """
    Computes n * x recursively using only addition.
    Formula: n * x = x + (n-1) * x
    
    Args:
        n: A positive integer (multiplier).
        x: An integer (multiplicand).
        
    Returns:
        The product of n and x.
    """
    # Base case: if n is 1, the result is x
    if n == 1:
        return x
    
    # Recursive step
    return x + recursive_multiplication(n - 1, x)

# Driver code
if __name__ == "__main__":
    n = 5
    x = 10
    print(f"{n} * {x} = {recursive_multiplication(n, x)}")