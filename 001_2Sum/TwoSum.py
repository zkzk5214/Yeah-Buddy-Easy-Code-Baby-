class Solution(object):
    def twoSum1(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """

        for num in nums:
            # Determine if (target - num_one) is in our nums list
            # These two numbers are different
            if target - num in nums and num is not target - num:
                # nums.index(4) = 0, nums.index(3) = 1
                return [nums.index(num), nums.index(target - num)]

    def twoSum2(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        # Create a dict
        lookup = {}  # {num:index}

        # For counter and value in nums
        for index, num in enumerate(nums):

            # If num2 = target - num1 already in the lookup dict
            # return the index1 and index2
            if target - num in lookup:
                return [lookup[target - num], index]

            # If not, put num with index in lookup
            lookup[num] = index
        # Return again
        return []


if __name__ == "__main__":
    nums = [4, 3, 5, 15]
    target = 7
    s = Solution()
    # print(s.twoSum1(nums, target))
    print(s.twoSum2(nums, target))
