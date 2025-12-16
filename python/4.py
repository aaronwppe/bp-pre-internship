# Prog. 004
# Write a function to find the largest integers from a given list of numbers using heap queue algorithm.


def insert_into_max_heap(heap: list[int], element: int) -> None:
    heap.append(element)

    node_idx = len(heap) - 1

    while node_idx > 0:
        parent_idx = (node_idx - 1) // 2

        parent_element = heap[parent_idx]
        node_element = heap[node_idx]

        if parent_element < node_element:
            heap[parent_idx], heap[node_idx] = node_element, parent_element

        node_idx = parent_idx


def largest(integers: list[int]) -> tuple[int]:
    heap = []

    for i in integers:
        insert_into_max_heap(heap, i)

    return heap[0]


if __name__ == "__main__":
    print(largest([1, 2, 3]))
