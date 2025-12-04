def gcd_recursive(a, b):
    """
    Computes the Greatest Common Divisor (GCD) of a and b
    using the Euclidean algorithm.
    Recursive step: gcd(a, b) = gcd(b, a % b)
    
    Args:
        a, b: Integers
    """
    # Base case: if b becomes 0, a is the GCD
    if b == 0:
        return a
    
    # Recursive step
    return gcd_recursive(b, a % b)

# Driver code to test the algorithm
if __name__ == "__main__":
    num1 = 48
    num2 = 18
    print(f"GCD of {num1} and {num2} is: {gcd_recursive(num1, num2)}")