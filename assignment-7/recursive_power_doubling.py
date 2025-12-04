def recursive_power_doubling(a, n):
    """
    Computes a^(2^n) recursively.
    Formula: a^(2^(n)) = (a^(2^(n-1)))^2
    This leverages the property that squaring the base doubles the exponent.
    
    Args:
        a: A real number.
        n: A non-negative integer.
        
    Returns:
        Result of a raised to the power of (2^n).
    """
    # Base case: When n = 0, exponent is 2^0 = 1. Result is a^1 = a.
    if n == 0:
        return a
    
    # Recursive step: Get result for n-1 and square it
    previous_result = recursive_power_doubling(a, n - 1)
    return previous_result * previous_result

# Driver code
if __name__ == "__main__":
    a = 3
    n = 2
    # Expect: 3^(2^2) = 3^4 = 81
    result = recursive_power_doubling(a, n)
    print(f"{a}^(2^{n}) = {result}")
    
    a = 2
    n = 3
    # Expect: 2^(2^3) = 2^8 = 256
    result = recursive_power_doubling(a, n)
    print(f"{a}^(2^{n}) = {result}")