# Prog. 478
# Write a function to remove lowercase substrings from a given string.


def remove_lowercase(string: str) -> str:
    ret_str = str()

    for s in string:
        if s.isupper():
            ret_str += s
    
    return ret_str

if __name__ == "__main__":
    s = "hello WORlD"

    print(remove_lowercase(s))