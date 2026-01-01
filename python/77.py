# Prog. 077
# Write a python function to find the difference between sum of even and odd digits.

def difference_of_sum_of_even_and_odd(array: list[int]) -> int:
    even_sum = 0
    odd_sum = 0

    for element in array:
        if element % 2 == 0:
            even_sum += element
        else:
            odd_sum += element

    return even_sum - odd_sum


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    print(difference_of_sum_of_even_and_odd(array))