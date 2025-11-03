# Prog. 703	
# Write a function to check whether the given key is present in the dictionary or not.

from typing import Any

def check_key(dictionary: dict, key: Any) -> bool:
    return key in dictionary

if __name__ == "__main__":
    d = {
        "1": 0,
        0: 2
    }

    print(check_key(d, "1"))