# Prog. 109
# Write a python function to find the count of rotations of a binary string with odd value.


def rotations_to_odd(binary_string: str) -> int:
    return binary_string.count('1')

if __name__ == '__main__':
    print(rotations_to_odd('0101'))
