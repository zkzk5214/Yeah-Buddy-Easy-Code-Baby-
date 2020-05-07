class Solution(object):

    def ThreeSum(self, nums):
        """
        :param nums: List[int]
        :return: List[int]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # prevent checking duplicate again
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:  # skip over same valued elements
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:  # skip over same valued elements
                        r -= 1
                    l += 1
                    r -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.ThreeSum([-1, 0, 1, 2, -1, -4]))