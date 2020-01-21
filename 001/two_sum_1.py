class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for num_one in nums:
            # Determine if (target - num_one) is in our nums list
            # These two numbers are different
            if target - num_one in nums and num_one is not target - num_one:
                # nums.index(4) = 0, nums.index(3) = 1
                return [nums.index(num_one), nums.index(target - num_one)]


nums = [4, 3, 5, 15]
target = 7
s = Solution()
print(s.twoSum(nums, target))

