def recursive_square(n):
    """
    Computes n^2 recursively using the expansion of (n-1)^2.
    Formula derived from (n+1)^2 = n^2 + 2n + 1 (as per problem statement),
    which can be rewritten for recursion as:
    n^2 = (n-1)^2 + 2(n-1) + 1
    
    Args:
        n: A non-negative integer.
        
    Returns:
        The square of n.
    """
    # Base case: 0^2 = 0
    if n == 0:
        return 0
    
    # Recursive step
    # n^2 = (n-1)^2 + 2*(n-1) + 1
    prev_square = recursive_square(n - 1)
    return prev_square + 2 * (n - 1) + 1

# Driver code
if __name__ == "__main__":
    n = 8
    # 8^2 = 64
    print(f"{n}^2 = {recursive_square(n)}")
    
    # Verify correctness for a small range
    print("Verifying first 5 squares:")
    for i in range(5):
        print(f"{i}^2 = {recursive_square(i)}")