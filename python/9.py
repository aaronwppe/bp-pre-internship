# Prog. 009
# Write a python function to find the minimum number of rotations required to get the same string.


def min_rotations(string: str) -> int:
    rotations = 0

    for partition_idx in range(len(string) - 1, -1, -1):
        rotations += 1

        if string == (string[partition_idx:] + string[:partition_idx]):
            break

    return rotations


def min_rotations_without_slicing(string: str) -> int:
    rotations = 0

    for partition_idx in range(len(string) - 1, -1, -1):
        rotations += 1

        if not _is_parition_a_match(string, 0, partition_idx, len(string)):
            continue

        if _is_parition_a_match(string, len(string) - partition_idx, 0, partition_idx):
            break

    return rotations


def _is_parition_a_match(
    string: str, string_start: int, parition_start: int, parition_stop: int
) -> bool:
    i = string_start

    for j in range(parition_start, parition_stop):
        if string[i] != string[j]:
            return False

        i += 1

    return True


if __name__ == "__main__":
    print(min_rotations_without_slicing("abcabc"))
