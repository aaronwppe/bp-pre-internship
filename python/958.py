# Prog. 958
# Write a function to convert an integer into a roman numeral.

# References:
# - https://www.youtube.com/watch?v=MOIJxae_7Pk

# NOT COMPLETE
# The math applied in the 'num < root' condition is incorrect.

# must be ordered
ROMAN_NUMERAL_SYMBOLS = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
}

MAX_ROMAN_NUMERAL = max(ROMAN_NUMERAL_SYMBOLS.keys())


def get_all_limits() -> tuple[int, ...]:
    ret = list()

    max_numeral = MAX_ROMAN_NUMERAL
    i = 1

    while i <= max_numeral:
        ret.append(i - (i // 10))
        ret.append(i * 4)
        i *= 10

    return tuple(ret[1:-1])


ALL_LIMITS: tuple[int, ...] = get_all_limits()


def _get_nearest_root_numeral(num: int) -> int:
    if num in ROMAN_NUMERAL_SYMBOLS:
        return num

    for limit, numeral in zip(ALL_LIMITS, ROMAN_NUMERAL_SYMBOLS.keys()):
        if num < limit:
            return numeral

    return MAX_ROMAN_NUMERAL


def get_roman_numeral(num: int) -> str | None:
    if num <= 0:
        return None

    left = ""
    right = ""

    root = _get_nearest_root_numeral(num)

    print(num, root)
    if num < root:
        x = root // 10

        left_num = (num // x) * x if x != 0 else num
        left = get_roman_numeral(root - left_num)

        if num != left_num:
            right = get_roman_numeral(num - left_num)

    root_multiple = max(num // root, 1)
    # Same as,
    # root_multiple = (num // root) if num > root else 1

    middle = ROMAN_NUMERAL_SYMBOLS[root] * root_multiple

    if num > root and (root * root_multiple) != num:
        right = get_roman_numeral(num - (root * root_multiple))

    return left + middle + right


if __name__ == "__main__":
    nums = [46]
    for n in nums:
        print(n, " = ", get_roman_numeral(n))

# ===================

# 1 - 3 = I ---------------------------------  1-4 -> (1 - (1//10), 1*4)
# 4 - 8 = I, V ------------------------------  4-9 ->
# 9 - 39 = I, V, X --------------------------  9-40 -> (10 - (10//10), 10*4)
# 40 - 89 = I, V, X, L ----------------------  40-90 ->
# 90 - 399 = I, V, X, L, C ------------------  90-400 -> (100 - (100//10), 100*4)

# 1 = I
# 5 = V
# 10 = X
# 50 = L
# 100 = C
# 500 = D
# 1000 = M

# 3 = III
# 7 = VII
# 17 = XVII
# 65 = LXV

# 157 = CLVII
# 276 = CCLXXVI

# 6 = VI
# 4 = IV
# 11 = XI
# 9 = IX
# 90 = XC
# 110 = CX

# 96 = XCVI
# 609 = DCIX
# 444 = CDXLIV

# 18 = XVIII
# 34 = XXXIV

# 176 = CLXXVI
# 97 = XCVII
# 1846 = MDCCCXLVI
