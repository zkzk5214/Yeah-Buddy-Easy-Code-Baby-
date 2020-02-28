class Solution(object):
    def removeElement(self, nums, val):
        """
        :param nums: List[int]
        :param val: int
        :return: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)


s = Solution()
nums = [3, 2, 2, 3]
val = 3
text = s.removeElement(nums, val)
print(text) #2
