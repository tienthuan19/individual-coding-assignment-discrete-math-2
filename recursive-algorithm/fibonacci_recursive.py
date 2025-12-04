def fibonacci_recursive(n):
    """
    Computes the nth Fibonacci number recursively.
    Sequence: 0, 1, 1, 2, 3, 5, 8...
    F(n) = F(n-1) + F(n-2)
    
    Args:
        n: A non-negative integer.
    """
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive step
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Driver code
if __name__ == "__main__":
    n = 7
    print(f"Fibonacci number at position {n} is: {fibonacci_recursive(n)}")