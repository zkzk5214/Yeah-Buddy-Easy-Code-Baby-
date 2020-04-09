from collections import Counter


def majorityElement(nums):
    count = Counter(nums)   # Counter({3: 2, 4: 2, 2: 1})
    res = []
    for i, f in count.items():
        if f > len(nums) / 3:
            res.append(i)
    return res


nums = [2, 3, 3, 4, 4]
print(majorityElement(nums))
