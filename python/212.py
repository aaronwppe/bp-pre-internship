# Prog. 212
# Write a python function to find the sum of fourth power of n natural numbers.

def sum_of_4th_power(limit: int) -> int | None:
    if limit < 0:
        return None
   
    if limit <= 1:
        return limit
    
    sum = 1

    for i in range(2, limit + 1):
        sum += i ** 4

    return sum

if __name__ == '__main__':
    print(sum_of_4th_power(5))