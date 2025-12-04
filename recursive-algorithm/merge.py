def merge(left, right):
    """
    Helper function to merge two sorted sub-lists.
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    """
    Sorts an array using the recursive Merge Sort algorithm.
    Divide and Conquer strategy.
    
    Args:
        arr: The list to sort.
    """
    # Base case: list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle point
    mid = len(arr) // 2
    
    # Recursively divide the halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left_half, right_half)

# Driver code
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original Array: {data}")
    sorted_data = merge_sort(data)
    print(f"Sorted Array:   {sorted_data}")