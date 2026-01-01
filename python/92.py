# Prog. 092
# Write a function to check whether the given number is undulating or not.

# Undulating Number:
# 1. 2 types of digits only
# 2. digits alternate
# 3. digit count >= 3 

def is_undulating(num: int) -> bool:
    num = abs(num)

    if num <= 99:
        return False

    digit_1 = num % 10
    num //= 10

    digit_2 = num % 10
    num //= 10

    if digit_1 == digit_2:
        return False
    
    odd_digit = True

    while num > 0:
        digit = num % 10
 
        if (odd_digit and digit != digit_1) or (not odd_digit and digit != digit_2):
            return False
        
        odd_digit = not odd_digit
        
        num //= 10

    return True

if __name__ == '__main__':
    print(is_undulating(9292))