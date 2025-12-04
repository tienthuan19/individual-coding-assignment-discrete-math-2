def recursive_min(arr, n):
    """
    Finds the minimum value in a list of n integers recursively.
    Logic: min(arr) = min(last_element, min(first_n-1_elements))
    
    Args:
        arr: A list of integers.
        n: The number of elements to consider (length of list).
        
    Returns:
        The minimum integer in the list.
    """
    # Base case: If there is only one element, it is the minimum
    if n == 1:
        return arr[0]
    
    # Recursive step: Find min of the first n-1 elements
    min_of_rest = recursive_min(arr, n - 1)
    
    # Compare the last element with the min of the rest
    if arr[n - 1] < min_of_rest:
        return arr[n - 1]
    else:
        return min_of_rest

# Driver code
if __name__ == "__main__":
    data = [12, 45, 67, 5, 23, 9, 88, 34]
    print(f"List: {data}")
    print(f"Minimum value is: {recursive_min(data, len(data))}")