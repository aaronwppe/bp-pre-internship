# Prog. 008
# Write a function to find squares of individual elements in a list using lambda function.


def get_squared_list(input_list: list[int]) -> list[int]:
    square = lambda x: x**2
    return [square(input_list[i]) for i in range(0, len(input_list))]


def get_squared_list_using_map(input_list: list[int]) -> list[int]:
    square = lambda x: x**2
    return list(map(square, input_list))


if __name__ == "__main__":
    print(get_squared_list_using_map([1, 2, 3]))
