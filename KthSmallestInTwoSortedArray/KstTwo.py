def KthSmallestinTwoSortedArray(arr1, arr2, k):
    """
    there is no difference between int and floor in positive num
    """
    if len(arr1) == 0:
        return arr2[k]
    elif len(arr2) == 0:
        return arr1[k]

    m1 = int(len(arr1) / 2)  # mid index of arr1
    m2 = int(len(arr2) / 2)
    
    if m1 + m2 < k:
        if arr1[m1] > arr2[m2]:
            return KthSmallestinTwoSortedArray(arr1, arr2[m2 + 1:], k - m2 - 1)
        else:
            return KthSmallestinTwoSortedArray(arr1[m1 + 1:], arr2, k - m1 - 1)
    else:
        if arr1[m1] > arr2[m2]:
            return KthSmallestinTwoSortedArray(arr1[:m1], arr2, k)
        else:
            return KthSmallestinTwoSortedArray(arr1, arr2[:m2], k)


if __name__ == "__main__":
    x = [1, 2, 3, 4, 6]
    y = [2, 3, 4]
    s = KthSmallestinTwoSortedArray(x, y, 4)
    print(s)
