class Solution(object):
    def removeElement1(self, nums, val):
        """
        :param nums: List[int]
        :param val: int
        :return: int
        O(n^2): remove or pop
        """
        while val in nums:
            nums.remove(val)
        return len(nums)

    def removeElement2(self, nums, val):
        """
        :param nums: List[int]
        :param val: int
        :return: int
        O(n)
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                # Change the target and the end, decrease the list
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1
        return start


if __name__ == "__main__":
    s = Solution()
    nums, val = [4, 2, 3, 1], 3
    text = s.removeElement1(nums, val)
    print(text)
