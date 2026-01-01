# Prog. 087
# Write a function to merge three dictionaries into a single expression.

# References:
# - https://www.geeksforgeeks.org/python/merge-two-dictionaries-in-a-single-expression-in-python/


def merge_dictionaries(*args: dict) -> dict:
    ret_dict = dict()

    for d in args:
        ret_dict.update(d)

    return ret_dict


if __name__ == '__main__':
    d1 = {1: "Hello"}
    d2 = {2: "World"}
    d3 = {1: "Hi"}
    
    print(merge_dictionaries(d1, d2, d3))
    print(d1 | d2 | d3)