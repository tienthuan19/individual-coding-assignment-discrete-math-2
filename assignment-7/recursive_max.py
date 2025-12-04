def recursive_max(arr, n):
    """
    Finds the maximum value in a list of n integers recursively.
    Logic: max(arr) = max(last_element, max(first_n-1_elements))
    
    Args:
        arr: A list of integers.
        n: The number of elements to consider (length of list).
        
    Returns:
        The maximum integer in the list.
    """
    # Base case: If there is only one element, it is the maximum
    if n == 1:
        return arr[0]
    
    # Recursive step: Find max of the first n-1 elements
    max_of_rest = recursive_max(arr, n - 1)
    
    # Compare the last element with the max of the rest
    if arr[n - 1] > max_of_rest:
        return arr[n - 1]
    else:
        return max_of_rest

# Driver code
if __name__ == "__main__":
    data = [12, 45, 67, 23, 9, 88, 34]
    print(f"List: {data}")
    print(f"Maximum value is: {recursive_max(data, len(data))}")