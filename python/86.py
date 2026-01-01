# Prog. 086
# Write a function to find nth centered hexagonal number.

# Chn = 3n(n − 1) + 1

def get_centered_hexagonal_number(n: int) -> int | None:
    if n <= 0:
        return None
    
    return (3 * n * (n - 1)) + 1


if __name__ == '__main__':
    print(get_centered_hexagonal_number(2))