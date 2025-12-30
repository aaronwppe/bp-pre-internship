# Prog. 48
# Write a python function to set all odd bits of a given number.


def set_odd_bits(num: int) -> int:
    binary_num = bin(num)

    ret_binary = "0b"
    is_odd = True

    for b in binary_num[:1:-1]:
        if is_odd:
            ret_binary += "1"
            is_odd = False
        else:
            ret_binary += b
            is_odd = True

    return int(ret_binary, 2)


if __name__ == "__main__":
    print(set_odd_bits(10))
