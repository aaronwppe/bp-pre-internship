# Prog. 21
# Write a function to find m number of multiples of n.


def get_multiples(num: int, count: int) -> list[int]:
    if count <= 0:
        return []

    return [num * i for i in range(1, count + 1)]


if __name__ == "__main__":
    print(get_multiples(5, 3))
