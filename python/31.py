# Prog. 31
# Write a function to find the top k integers that occur most frequently
# from given lists of sorted and distinct integers using heap queue algorithm.

# list and tuples are compared lexographically

import heapq


def get_k_frequent(k: int, *args: list[int]) -> list[int]:
    if k <= 0 or not args:
        return []

    freq = {element: 1 for element in args[0]}

    for l in args[1:]:
        for element in l:
            if element not in freq:
                freq[element] = 1
            else:
                freq[element] += 1

    heap_queue = []

    for element, occ in freq.items():
        heapq.heappush(heap_queue, (occ, element))

        if len(heap_queue) > k:
            heapq.heappop(heap_queue)

    heap_queue.sort(reverse=True)

    return [element for _, element in heap_queue]


if __name__ == "__main__":
    l1 = [1, 2, 3, 4]
    l2 = [1, 3, 4]
    l3 = [1, 2, 3]

    print(get_k_frequent(2, l1, l2, l3))
