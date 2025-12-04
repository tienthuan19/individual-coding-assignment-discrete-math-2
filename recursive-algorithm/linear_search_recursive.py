def linear_search_recursive(arr, target, index=0):
    """
    Recursively searches for a target in a list.
    
    Args:
        arr: The list to search through.
        target: The value to find.
        index: The current index being checked (default 0).
        
    Returns:
        Index of target if found, otherwise -1.
    """
    # Base case 1: If index reaches the end of list, element not found
    if index >= len(arr):
        return -1
    
    # Base case 2: If element is found at current index
    if arr[index] == target:
        return index
    
    # Recursive step: Check the next index
    return linear_search_recursive(arr, target, index + 1)

# Driver code
if __name__ == "__main__":
    data = [10, 50, 30, 70, 80, 20]
    item = 30
    result = linear_search_recursive(data, item)
    
    if result != -1:
        print(f"Element {item} found at index {result}")
    else:
        print(f"Element {item} not found")