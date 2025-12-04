def merge_two_sorted_lists(list1, list2):
    """
    Merges two sorted lists into a single sorted list.
    
    Args:
        list1: First sorted list.
        list2: Second sorted list.
    
    Returns:
        A new combined sorted list.
    """
    result = []
    i = 0 # Pointer for list1
    j = 0 # Pointer for list2
    
    # Compare elements and append the smaller one
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
            
    # Append remaining elements from list1 (if any)
    while i < len(list1):
        result.append(list1[i])
        i += 1
        
    # Append remaining elements from list2 (if any)
    while j < len(list2):
        result.append(list2[j])
        j += 1
        
    return result

# Driver code
if __name__ == "__main__":
    left_list = [1, 3, 5, 7]
    right_list = [2, 4, 6, 8]
    print(f"Merged List: {merge_two_sorted_lists(left_list, right_list)}")