# Prog. 25
# Write a python function to find the product of non-repeated elements in a given array.


def product_of_distinct(array: list[float | int]) -> int | float | None:
    if not array:
        return None

    num_set = set()
    product = 1

    for num in array:
        if num not in num_set:
            num_set.add(num)
            product *= num

    return product


if __name__ == "__main__":
    print(product_of_distinct([1, 2, 1, 3]))
