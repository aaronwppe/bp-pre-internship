# Prog. 279	
# Write a function to find the nth decagonal number.

def get_decagonal_number(n: int) -> int:
    return (4 * (n ** 2)) - (3 * n)

if __name__ == "__main__":
    num = 3

    decagonal_num = get_decagonal_number(num)
    print(decagonal_num)