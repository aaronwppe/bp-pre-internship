# Prog. 123
# Write a function to sum all amicable numbers from 1 to a specified number.


def get_sum_of_amicable_nums(n: int):
    n += 1
    proper_divisor_sums = [0] * n

    for i in range(1, n):
        for j in range(i * 2, n, i):
            proper_divisor_sums[j] += i

    amicable_sum = 0

    for lower_num in range(1, n):
        higher_num = proper_divisor_sums[lower_num]

        if (
            (higher_num < n)
            and (higher_num > lower_num)
            and (lower_num == proper_divisor_sums[higher_num])
        ):
            amicable_sum = lower_num + higher_num

    return amicable_sum


if __name__ == "__main__":
    print(get_sum_of_amicable_nums(500))
