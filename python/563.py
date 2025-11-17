# Prog. 563
# Write a function to extract values between quotation marks of a string.


def get_str_within(string: str, target: str = '"') -> list[str]:
    index_ranges: list[list[int, int]] = []
    is_prev_range_open = False

    for i in range(0, len(string)):
        if string[i] != target:
            continue
        
        if is_prev_range_open == False:
            index_ranges.append([i])
            is_prev_range_open = True
            continue

        index_ranges[-1].append(i)
        is_prev_range_open = False

    if is_prev_range_open == True and index_ranges:
        index_ranges.pop()

    return [
        string[index_range[0] + 1 : index_range[1]]
        for index_range in index_ranges
    ]

if __name__ == "__main__":
    print(get_str_within('hello "world" "this is another example"""'))