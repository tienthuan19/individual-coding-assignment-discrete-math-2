def binary_search_recursive(arr, low, high, target):
    """
    Recursively performs binary search on a sorted list.
    
    Args:
        arr: Sorted list of elements.
        low: Lower index bound.
        high: Upper index bound.
        target: Value to search for.
    
    Returns:
        Index of target if found, -1 otherwise.
    """
    # Base case: If boundaries cross, element is not present
    if high < low:
        return -1

    # Calculate middle index
    mid = (low + high) // 2

    # Case 1: Target is at the middle
    if arr[mid] == target:
        return mid
    
    # Case 2: Target is smaller than mid, search left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, low, mid - 1, target)
    
    # Case 3: Target is larger than mid, search right half
    else:
        return binary_search_recursive(arr, mid + 1, high, target)

# Driver code
if __name__ == "__main__":
    sorted_data = [2, 3, 4, 10, 40]
    target_val = 10
    
    # Initial call passes 0 as low and len-1 as high
    result = binary_search_recursive(sorted_data, 0, len(sorted_data) - 1, target_val)
    
    if result != -1:
        print(f"Element {target_val} found at index {result}")
    else:
        print(f"Element {target_val} not found")