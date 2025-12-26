# Prog. 035
# Write a function to find the n-th rectangular number.


def get_rectangluar_number(n: int) -> int | None:
    if n <= 0:
        return None

    return n**2 + n


if __name__ == "__main__":
    print(get_rectangluar_number(4))
