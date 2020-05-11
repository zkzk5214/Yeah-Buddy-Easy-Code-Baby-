def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    merged = []

    mid = len(arr) // 2
    l = mergeSort(arr[:mid])    # Recursively divide
    r = mergeSort(arr[mid:])

    while l and r:  # Sort
        if l[0] <= r[0]:
            merged.append(l.pop(0))
        else:
            merged.append(r.pop(0))
    # Add the last(biggest) value in the merged list
    merged.extend(r if r else l)
    return merged   # Return and Merge


if __name__ == '__main__':
    with open('1.txt', 'r') as f:
        for i in f.readlines():
            input_list = list(map(int, i.split()))

    s = mergeSort(input_list)

    listToStr = ' '.join(map(str, s))
    print(listToStr)
