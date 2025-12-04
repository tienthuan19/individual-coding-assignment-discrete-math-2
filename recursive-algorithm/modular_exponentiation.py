def modular_exponentiation(b, n, m):
    """
    Computes (b^n) mod m recursively.
    Uses the property: (A*B) % m = ((A % m) * (B % m)) % m
    For efficiency (O(log n)), we use the squaring method:
    - If n is even: (b^(n/2))^2 % m
    - If n is odd:  (b * b^(n-1)) % m
    
    Args:
        b: Integer base (1 <= b < m)
        n: Integer exponent (n >= 0)
        m: Integer modulus (m >= 2)
    """
    if n == 0:
        return 1
    
    if n % 2 == 0:
        # If n is even, calculate result for n/2 and square it
        half_power = modular_exponentiation(b, n // 2, m)
        return (half_power * half_power) % m
    else:
        # If n is odd, multiply base with result of n-1
        return (b * modular_exponentiation(b, n - 1, m)) % m

# Driver code to test the algorithm
if __name__ == "__main__":
    b, n, m = 3, 4, 5
    # 3^4 = 81. 81 mod 5 = 1
    print(f"{b}^{n} mod {m} = {modular_exponentiation(b, n, m)}")