# Prog. 106
# Write a function to add the given list to the given tuples.

from typing import Any

def add_to_tuples(tuples: list[tuple[Any, ...]], input_list: list[Any]) -> None:
    for i, t in enumerate(tuples):
        li = list(t)
        li.append(input_list)
        tuples[i] = tuple(li)

    
if __name__ == '__main__':
    list_of_tuples = [(1, 2,), (3, 4)]
    append_list = [5, 6]
    add_to_tuples(list_of_tuples, append_list)
    print(list_of_tuples)