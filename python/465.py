# Prog. 465
# Write a function to drop empty items from a given dictionary.

from typing import Any

def drop_items(d: dict, value: Any = None) -> None:
    keys = list(d.keys())

    for key in keys:
        if d[key] == value:
            d.pop(key)


if __name__ == "__main__":
    d = {
        "a": 1,
        "b": None,
        "c": None
    }

    drop_items(d)
    print(d)