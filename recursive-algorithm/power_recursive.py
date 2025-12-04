def power_recursive(a, n):
    """
    Computes a^n recursively.
    Formula: a^n = a * a^(n-1)
    
    Args:
        a: A nonzero real number (base).
        n: A nonnegative integer (exponent).
        
    Returns:
        The result of a raised to the power of n.
    """
    # Base case: any number to the power of 0 is 1
    if n == 0:
        return 1
    
    # Recursive step
    return a * power_recursive(a, n - 1)

# Driver code to test the algorithm
if __name__ == "__main__":
    base = 2.0
    exponent = 3
    print(f"{base} raised to power {exponent} is: {power_recursive(base, exponent)}")
    
    print(f"5 raised to power 0 is: {power_recursive(5, 0)}")