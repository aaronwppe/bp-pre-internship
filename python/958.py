# Prog. 958
# Write a function to convert an integer into a roman numeral.

# References:
# - https://www.youtube.com/watch?v=MOIJxae_7Pk
# - https://leetcode.com/problems/integer-to-roman/

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


def get_roman_numeral(num: int) -> str | None:
    if num <= 0:
        return None

    left = ""
    right = ""

    root = _get_nearest_root_numeral(num)

    if num < root:
        left_num = _get_left_num(num)
        right_num = num - left_num

        left = get_roman_numeral(root - left_num)
        right = get_roman_numeral(right_num) if right_num != 0 else ""

    multipler = max(num // root, 1)
    middle = ROMAN_NUMERAL_SYMBOLS[root] * multipler

    mid_num = root * multipler
    if num > mid_num:
        right = get_roman_numeral(num - mid_num)

    return left + middle + right


def _get_nearest_root_numeral(num: int) -> int:
    if num in ROMAN_NUMERAL_SYMBOLS:
        return num

    for limit, numeral in zip(ALL_LIMITS, ROMAN_NUMERAL_SYMBOLS.keys()):
        if num < limit:
            return numeral

    return MAX_ROMAN_NUMERAL


def _get_left_num(num: int) -> tuple[int, int]:
    count = 0
    digit = num

    while num > 0:
        count += 1
        digit = num % 10
        num //= 10

    return digit * 10 ** (count - 1)


LEFT_MOST_ROMAN_NUMERALS = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


# this solution is taken from 'leetcode'
def get_roman_numeral_2(num: int) -> str | None:
    if num <= 0:
        return None

    ret = ""

    for value, symbol in LEFT_MOST_ROMAN_NUMERALS:
        ret += symbol * (num // value)
        num %= value

    return ret


if __name__ == "__main__":
    nums_1 = [1, 5, 10, 50, 100, 500, 1000]
    nums_2 = [3, 7, 17, 65, 157, 276]
    nums_3 = [6, 4, 11, 9, 90, 110]
    nums_4 = [96, 609, 444, 18, 34]
    nums_5 = [176, 97, 1846]

    for num in nums_5:
        print(f"{num} = {get_roman_numeral_2(num)}")

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
