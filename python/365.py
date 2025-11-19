# Prog. 365
# Write a python function to count the number of digits of a given number.

def get_digit_count(num: int) -> int:
    num = abs(num)
    multiplier = 10
    count = 1
    
    while num >= multiplier:
        count += 1
        multiplier *= 10

    return count

if __name__ == "__main__":
    print(get_digit_count(999))