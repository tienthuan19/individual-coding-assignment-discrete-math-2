def recursive_mult_halving(x, y):
    """
    Computes x * y recursively based on the properties:
    - xy = 2 * (x * (y/2))      if y is even
    - xy = 2 * (x * [y/2]) + x  if y is odd
    - xy = 0                    if y = 0
    
    This is effectively the 'Russian Peasant Multiplication' logic adapted recursively.
    
    Args:
        x: Non-negative integer.
        y: Non-negative integer.
        
    Returns:
        The product of x and y.
    """
    # Base case
    if y == 0:
        return 0
    
    # Recursive step: compute result for y // 2
    half_product = recursive_mult_halving(x, y // 2)
    
    # If y is even: 2 * half_product
    if y % 2 == 0:
        return 2 * half_product
    # If y is odd: 2 * half_product + x
    else:
        return 2 * half_product + x

# Driver code
if __name__ == "__main__":
    x = 15
    y = 6
    # 15 * 6 = 90
    print(f"{x} * {y} = {recursive_mult_halving(x, y)}")
    
    x = 20
    y = 5
    # 20 * 5 = 100
    print(f"{x} * {y} = {recursive_mult_halving(x, y)}")