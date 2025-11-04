# Prog. 706
# Write a function to find whether an array is subset of another array.

# References:
# - https://www.w3schools.com/python/python_sets_join.asp


from typing import Any

# Works with duplicates elements. Limitation: All array elements must be of an immutable type.
def is_subset(array: list[Any], subset_array: list[Any]) -> bool:
    if len(subset_array) > len(array):
        return False
    
    frequency_map = dict()
    for key in subset_array:
        if key in frequency_map:
            frequency_map[key] += 1
        else:
            frequency_map[key] = 1

    for element in array:
        if element in frequency_map:
            frequency_map[element] -= 1
    
    return all(value <= 0 for value in frequency_map.values())

# Faster but will not work with arrays that contain duplicate elements
def is_subset_using_sets(array: list[Any], subset_array: list[Any]) -> bool:
    array_sub_set = set(subset_array)
    return len(array_sub_set.intersection(array)) == len(array_sub_set)

if __name__ == "__main__":
    array = [1, 4, 2, 3, 5, 6, 3, 3]
    subset_array = [1, 2, 3, 3]

    ret_bool = is_subset_using_sets(array, subset_array)
    print(ret_bool)