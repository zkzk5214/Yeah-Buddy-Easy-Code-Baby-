def heapSort(list):
    n = len(list)

    # Build_Max_Heap
    startIdx = int((n / 2)) - 1
    for i in range(startIdx, -1, -1):  # Last non-leaf node
        MaxHeapify(list, n, i)

    # Sort: swap the first and the last, size--
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        MaxHeapify(list, i, 0)


def MaxHeapify(list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2 

    # Left child
    if left < n and list[left] > list[largest]:
        largest = left
    # Right child
    if right < n and list[right] > list[largest]:
        largest = right
    # Root is the largest
    if largest != i:
        temp = list[i]
        list[i] = list[largest]
        list[largest] = temp
        # Recursively
        MaxHeapify(list, n, largest)


def printHeap(list):
    n = len(list)
    for i in range(n):
        print(list[i], end=" ")
    print()


if __name__ == '__main__':
    with open('1.txt', 'r') as f:
        for i in f.readlines():
            input_list = list(map(int, i.split()))
            heapSort(input_list)
            printHeap(input_list)
