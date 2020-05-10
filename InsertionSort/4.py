def InsertionSort(nums):
    count = 0
    for i in range(2, len(nums) + 1):
        k = i
        while k > 1 and nums[k - 1] < nums[k - 2]:
            nums[k - 2], nums[k - 1] = nums[k - 1], nums[k - 2]  # Swap
            count += 1
            k -= 1

    return count


if __name__ == "__main__":
    with open('1.txt', 'r') as f:
        for i in f.readlines():
            input_list = list(map(int, i.split()))

print(InsertionSort(input_list))
