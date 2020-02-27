class Solution(object):
    def maxArea(self, height):
        """
        :param height: List[int]
        :return: int
        """
        left = 0
        right = len(height) - 1
        Max = 0

        while left != right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left += 1
            else:
                area = height[right] * (right - left)
                right -= 1
            Max = max(area, Max)
        return Max


s = Solution()
text = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(text)
