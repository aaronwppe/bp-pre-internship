# Prog. 597
# Write a function to find kth element from the given two sorted arrays.

# References
# - https://youtu.be/nv7F4PiLUzo?si=IMcgSRSYXQV2-aia

import math


def get_kth_element(array_1: list[int], array_2: list[int], k: int) -> int | None:
    if k < 0 or (len(array_1) + len(array_2) <= k):
        return None
    
    i = 0
    j = 0
    element: int | None = None

    while k >= 0:
        if i < len(array_1) and array_1[i] < array_2[j]:
            element = array_1[i]
            i += 1

        elif j < len(array_2):
            element = array_2[j]
            j += 1

        else:
            element = None
            break
        
        k -= 1

    return element


# Solution from 'take U forward'
# Notes:
#   - Always perform binary search on the smaller of the 2 input arrays
#   - Generate partitions such that array_1 = [..., l1] + [r1, ...] and array_2 = [..., l2] + [r2, ...]
#   - Also, left_partition_1 + left_partition_2 = k 
#   - Iterate to satisfy condition (l1 <= r2 and l1 <= r1) 
#   - Using infinity / MAX_VALUE, handle edge cases where paritions may be empty.

def get_kth_element_using_binary_search(array_1: list[int], array_2: list[int], k: int) -> int | None:
    if k >= (len(array_1) + len(array_2)) or k < 0:
        return None
    
    if len(array_1) > len(array_2):
        array_1, array_2 = array_2, array_1

    low = max(0, k - len(array_2) - 1)  # inclusive
    # may alternatively be written as,
    # low = k - len(array_2) - 1 if len(array_2) < k else 0

    high = min(len(array_1), k + 1)  # exclusive
    # high = k + 1 if k + 1 < len(array_1) else len(array_1)

    while low < high:
        mid_1 = (low + high) // 2
        mid_2 = k - mid_1 - 1

        l1 = array_1[mid_1]
        r1 = array_1[mid_1 + 1] if mid_1 + 1 < len(array_1) else math.inf

        l2 = array_2[mid_2] if mid_2 >= 0 else -math.inf
        r2 = array_2[mid_2 + 1] if mid_2 + 1 < len(array_2) else math.inf

        if l1 > r2:
            high = mid_1
            
        elif l2 > r1:
            low = mid_1 + 1

        else:   # (l1 <= r2 and l1 <= r1) 
            return max(l1, l2)
    
    # case where elements in array_1 > elements in array_2
    return array_2[k]

if __name__ == "__main__":
    array_1 = [1, 4, 8, 10, 12]
    array_2 = [5, 7, 11, 15, 17]

    # 1, 4, 5, 7, 8, 10, 11, 12, 15, 17

    # both functions assume k is 0-indexed
    
    print(get_kth_element_using_binary_search(array_1, array_2, 3))     # 11
    print(get_kth_element_using_binary_search(array_1, array_2, 100))   # None