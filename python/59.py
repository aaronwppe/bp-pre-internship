# Prog. 059
# Write a function to find the nth octagonal number.


def get_octagonal_num(n: int) -> int | None:
    if n < 0:
        return None

    return (3 * n**2) - (2 * n)


if __name__ == "__main__":
    print(get_octagonal_num(5))


# (3n**2 - 2n)
