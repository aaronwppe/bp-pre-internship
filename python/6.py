# Prog. 006
# Write a python function to check whether the two numbers differ at one bit position only or not.


def differ_at_one_bit(n1: int, n2: int) -> bool:
    xor = n1 ^ n2
    return (xor & (xor - 1)) == 0 and xor != 0


if __name__ == "__main__":
    print(differ_at_one_bit(5, 7))
