def TwoWayPartition(nums):
    pivot = nums[0]
    left = []
    right = []
    for num in nums[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    return left + [pivot] + right


def ThreeWayPartition(nums):
    pivot = nums[0]
    small, equal, large = [], [], []

    for num in nums:
        if num < pivot:
            small.append(num)
        elif num > pivot:
            large.append(num)
        else:
            equal.append(num)

    return small + equal + large


if __name__ == '__main__':
    with open('1.txt', 'r') as f:
        for i in f.readlines():
            data = list(map(int, i.split()))
            partition = TwoWayPartition(data)
            print(' '.join(map(str, partition)))
