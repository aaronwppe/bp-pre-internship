# Prog. 321
# Write a function to find the demlo number for the given number.

# References:
# - https://www.scribd.com/document/36504170/Kaprekar-s-Demlo-Numbers
#   Page number: 5 - the point labelled as '(4)'

# Note:
# Here I will assume that, 
# for a -ve input I am allowed to process it just like it's +ve mirror
# and return it back in -ve

# c-style
def get_demlo_num(num: int) -> int:
    if num < 0:
        num *= -1
        is_negative = True
    else:
        is_negative = False

    demlo_num = num
    i = 10

    while num > i:
        left = num // i
        right = num % i

        j = left
        while j > 0:
            right *= 10
            j //= 10

        demlo_num += right + left
        i *= 10

    return demlo_num if is_negative == False else -demlo_num

# pythonic
def get_demlo_num_using_str(num: int) -> int:
    num_str = str(abs(num))

    demlo = 0

    for i in range(len(num_str)):
        demlo += int(f"{num_str[i:]}{num_str[:i]}")

    return demlo if num >= 0 else -demlo


if __name__ == "__main__":
    num = 3461
    print(get_demlo_num(num))