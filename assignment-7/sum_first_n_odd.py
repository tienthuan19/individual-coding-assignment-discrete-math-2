def sum_first_n_odd(n):
    """
    Computes the sum of the first n odd positive integers recursively.
    The nth odd integer is (2*n - 1).
    Formula: sum_odd(n) = (2*n - 1) + sum_odd(n-1)
    
    Args:
        n: A positive integer.
        
    Returns:
        The sum of the first n odd integers (1 + 3 + 5 + ...).
    """
    # Base case: The first odd integer is 1
    if n == 1:
        return 1
    
    # Recursive step
    current_odd = 2 * n - 1
    return current_odd + sum_first_n_odd(n - 1)

# Driver code
if __name__ == "__main__":
    n = 5
    # Expecting 1+3+5+7+9 = 25
    print(f"Sum of first {n} odd integers is: {sum_first_n_odd(n)}")