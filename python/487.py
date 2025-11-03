# Prog. 487
# Write a function to sort a list of tuples in increasing order by the last element in each tuple.

# References:
# - https://www.w3schools.com/dsa/dsa_algo_selectionsort.php

def sort(tuples: list[tuple[int, ...]]) -> None:
    for current_idx in range(len(tuples) - 1):
        min_idx = current_idx

        if not tuples[min_idx]:
            continue

        for comp_idx in range(current_idx + 1, len(tuples)):
            comp_tuple = tuples[comp_idx]

            if not comp_tuple:
                min_idx = comp_idx
                break

            if comp_tuple[-1] < tuples[min_idx][-1]:
                min_idx = comp_idx

        tuples[current_idx], tuples[min_idx] = tuples[min_idx], tuples[current_idx]


if __name__ == "__main__":
    list_of_tuples = [
        (1, 2, 3),
        tuple(),
        (1, 4),
        (2,)   
    ]

    sort(list_of_tuples)
    print(list_of_tuples)