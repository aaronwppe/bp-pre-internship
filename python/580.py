# Prog. 580
# Write a function to extract the even elements in the nested mixed tuple.


from typing import Any

def is_even(value: Any) -> bool:
    return type(value) is int and value % 2 == 0

def get_even_elements(input_tuple: tuple[Any, ...]) -> list[int]:
    ret_list = list()

    for element in input_tuple:
        if type(element) in (tuple, list, set):
            ret_list.extend(get_even_elements(element))

        elif is_even(element):
            ret_list.append(element)

    return ret_list

if __name__ == "__main__":
    my_tuple = (
        (1, 2, 3),
        ("str", 1),
        tuple(),
        [6],
        {10, 12}
    )

    print(get_even_elements(my_tuple))