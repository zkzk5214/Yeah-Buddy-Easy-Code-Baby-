def BinarySearch(array, key):
    left = 0
    right = len(array) - 1
    while True:
        mid = int((left + right) / 2)
        if array[mid] > key:
            right = mid - 1
        elif array[mid] < key:
            left = mid + 1
        elif array[mid] == key:
            return mid


if __name__ == '__main__':
    print(BinarySearch([1, 2, 3, 34, 56, 57, 78, 87], 87))
