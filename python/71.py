# Prog. 071
# Write a function to sort a list of elements using comb sort.

# References:
# - https://www.geeksforgeeks.org/dsa/comb-sort/

def get_next_gap(current_gap: int) -> int:
    gap = int(current_gap / 1.3)

    if gap == 0:
        return 1
    
    return gap

def comb_sort(array: list[int], reverse: bool = False): 
    is_greater_check = lambda x, y: x > y
    is_lesser_check = lambda x, y: x < y
    
    comparator = is_lesser_check if reverse else is_greater_check

    gap = len(array)
    did_swap = True

    while did_swap and gap > 1:
        gap = get_next_gap(gap)
        did_swap = False

        for i in range(len(array) - gap):
            if comparator(array[i], array[i + gap]):
                array[i], array[i + gap] = array[i + gap], array[i]
                did_swap = True
    

if __name__ == '__main__':
    array = [1, 3, 5, 7]
    comb_sort(array, reverse=True)
    print(array)