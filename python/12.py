# Prog. 012
# Write a function to sort a given matrix in ascending order according to the sum of its rows.


def sort_matrix_rows_by_sum(matrix: list[list[int]]) -> None:
    row_sums = []

    r = 0
    while r < len(matrix):
        row_sum = sum(matrix[r])

        i = 0
        while i < len(row_sums):
            if row_sum < row_sums[i]:
                matrix[r], matrix[i] = matrix[i], matrix[r]
                r -= 1
                break

            i += 1

        row_sums.insert(i, row_sum)
        r += 1


def sort_matrix_rows_by_sum_2(matrix: list[list[int]]) -> None:
    matrix.sort(key=sum)


if __name__ == "__main__":
    matrix = [
        [2, 3, 4],
        [3, 4, 1],
        [4, 3, 2],
    ]

    sort_matrix_rows_by_sum(matrix)

    print(matrix)
