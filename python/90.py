# Prog. 090
# Write a python function to find the length of the longest word.

def get_longest_word_len(string: str) -> int:
    word_boundaries = [' ', '\n', '\t']
    max_len = 0
    last_word_boundary_index = 0

    for i, s in enumerate(string + " "):
        if s not in word_boundaries:
            continue

        word_len = i - last_word_boundary_index
        if word_len == 0:
            continue

        last_word_boundary_index = i + 1

        if word_len > max_len:
            max_len = word_len

    return max_len


if __name__ == '__main__':
    string = "Hello World2"
    print(get_longest_word_len(string))
