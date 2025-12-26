# Prog. 41
# Write a function to filter even numbers using lambda function.

if __name__ == "__main__":
    filter_even_nums = lambda input_list: [num for num in input_list if num % 2 != 0]

    odd_list = filter_even_nums([1, 2, 3, 4])
    print(odd_list)
