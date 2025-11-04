# Prog. 384
# Write a python function to find the frequency of the smallest value in a given array.


def min_element_frequency(elements: list[int]) -> int | None:
    if not elements:
        return None
    
    min_element = elements[0]
    frequency = 1
    
    if len(elements) == 1:
        return frequency

    for element in elements[1:]:
        if element == min_element:
            frequency += 1

        elif element < min_element:
            min_element = element
            frequency = 1

    return frequency

if __name__ == "__main__":
    array = [-2, 1, 2, -1, 1, 0, -1]

    print(min_element_frequency(array))
