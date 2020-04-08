def majorityElement(nums):
    return sorted(nums)[len(nums) // 2]


nums = [2, 3, 2]
s = majorityElement(nums)
print(s)
