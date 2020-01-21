class Solution(object):
    def twoSum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        # Create an dict
        lookup = {}
        # for counter and value in nums
        for i, num in enumerate(nums):
            # if num2 = target - num1 already in the lookup dict
            if target - num in lookup:
                # return the index1 and index2
                return [lookup[target - num], i]
            # if not put num with index in lookup
            lookup[num] = i
        # return again
        return []


nums = [4, 3, 5, 15]
target = 8
s = Solution()
print(s.twoSum(nums, target))
