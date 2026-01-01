# Prog. 076
# Write a python function to count the number of squares in a rectangle.

def get_square_count(rows: int, cols: int) -> int:
    if rows <=0 or cols <= 0:
        return 0
    
    count = 0

    while rows > 0 or cols > 0:
        count += rows * cols
        rows -= 1
        cols -= 1

    return count


if __name__ == '__main__':
    print(get_square_count(4, 3))
    print(get_square_count(2, 2))


# Count of squares,
# 1x1 = rxc
# 2x2 = (r-1)x(c-1)
# 3x3 = (r-2)x(c-2)
# ...
# nxn = (r-(n-1))x(c-(n-1))