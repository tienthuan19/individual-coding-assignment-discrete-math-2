def sum_first_n(n):
    """
    Computes the sum of the first n positive integers recursively.
    Formula: sum(n) = n + sum(n-1)
    
    Args:
        n: A positive integer.
        
    Returns:
        The sum of 1 + 2 + ... + n.
    """
    # Base case: sum of first 1 integer is 1
    if n == 1:
        return 1
    
    # Recursive step
    return n + sum_first_n(n - 1)

# Driver code
if __name__ == "__main__":
    n = 10
    print(f"Sum of first {n} integers is: {sum_first_n(n)}")