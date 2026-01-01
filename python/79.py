# Prog. 079
# Write a python function to check whether the length of the word is odd or not.

def is_odd_length(word: str) -> bool:
    return len(word) % 2 != 0

if __name__ == '__main__':
    word = "hello"
    print(is_odd_length(word))