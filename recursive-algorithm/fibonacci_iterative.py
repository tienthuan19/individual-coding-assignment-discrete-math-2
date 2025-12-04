def fibonacci_iterative(n):
    """
    Computes the nth Fibonacci number using iteration (Loop).
    This is much more efficient than the naive recursive version.
    
    Args:
        n: A non-negative integer.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
        
    a, b = 0, 1
    
    # Loop from 2 to n
    for _ in range(2, n + 1):
        a, b = b, a + b
        
    return b

# Driver code
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci number at position {n} (Iterative) is: {fibonacci_iterative(n)}")