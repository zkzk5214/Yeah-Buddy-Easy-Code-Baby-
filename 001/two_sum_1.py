class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for num in nums:
            # Determine if (target - num_one) is in our nums list
            # These two numbers are different
            if target - num in nums and num is not target - num:
                # nums.index(4) = 0, nums.index(3) = 1
                return [nums.index(num), nums.index(target - num)]


nums = [4, 3, 5, 15]
target = 7
s = Solution()
print(s.twoSum(nums, target))
