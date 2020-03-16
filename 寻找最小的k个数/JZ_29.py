# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution1(self, nums, k):
        # write code here
        if nums == [] or k > len(nums):
            return []
        nums.sort()
        return nums[: k]

    def GetLeastNumbers_Solution2(self, nums, k):
        # write code here
        # 快排
        def quick_sort(lst):
            if not lst:
                return []
            pivot = lst[0]
            left = quick_sort([x for x in lst[1:] if x < pivot])
            right = quick_sort([x for x in lst[1:] if x >= pivot])
            return left + [pivot] + right

        if nums == [] or k > len(nums):
            return []
        results = quick_sort(nums)
        return results[: k]
