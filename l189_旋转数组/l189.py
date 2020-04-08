class Solution:
    def rotate1(self, nums, k):
        n = len(nums)
        k %= n
        for num in range(k):
            nums.insert(0, nums.pop())
        return nums

    def rotate2(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]
        return nums


s = Solution()

print(s.rotate1([1, 2, 3, 4, 5], 3))
