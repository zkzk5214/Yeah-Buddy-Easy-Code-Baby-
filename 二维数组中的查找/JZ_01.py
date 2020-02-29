class Solution(object):
    def Find(self, nums, target):
        """
        :param nums: List[int1,int2]
        :param target: int
        :return:True or False
        """
        row = len(nums)  # the number of the row
        column = len(nums[0])  # the length of the first row
        i = 0
        j = column - 1

        while i < row and j >= 0:
            if nums[i][j] > target:
                j -= 1
            elif nums[i][j] < target:
                i += 1
            else:
                return True
        return False

