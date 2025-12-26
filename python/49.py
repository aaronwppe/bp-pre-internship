# Prog. 49
# Write a function to extract every first or specified element from a given two-dimensional list.

from typing import Any


def extract_col(matrix: list[list[Any]], col: int = 0) -> list[Any]:
    return [row[col] if -len(row) <= col < len(row) else None for row in matrix]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [3, 4, 5], [1]]

    print(extract_col(matrix, col=-1))
