class Solution(object):
    def maxArea(self, height):
        """
        :param height: List[int]
        :return: int
        Width: We set two pointers, which are initialized as 0 and len(height) - 1
        to get the max width.
        Height: We move the left pointer and right pointer respectively
        to search for the next higher height.
        """
        
        l, r, area = 0, len(height) - 1, 0
        while l < r:
            h = min(height[l], height[r])
            area, l, r = max(area, h * (r - l)), l + (height[l] == h), r - (height[r] == h)
        return area


if __name__ == "__main__":
    s = Solution()
    text = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(text)
