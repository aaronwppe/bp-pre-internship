# Prog. 080
# Write a function to find the nth tetrahedral number.

# Tn = (n * (n + 1) * (n + 2)) / 6

def get_tetrahedral_number(n: int) -> int | None:
    if n < 0:
        return None
    
    return (n * (n + 1) * (n + 2)) // 6


if __name__ == '__main__':
    print(get_tetrahedral_number(5))
