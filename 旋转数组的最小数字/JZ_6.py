class Solution(object):
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return None
        if len(rotateArray) == 2:
            return rotateArray[1]
        elif len(rotateArray) == 0:
            return 0

        mid = int(len(rotateArray) / 2)
        if rotateArray[mid] > rotateArray[0]:
            return self.minNumberInRotateArray(rotateArray[mid:])
        elif rotateArray[mid] < rotateArray[0]:
            return self.minNumberInRotateArray(rotateArray[:mid + 1])
        else:
            return self.minNumberInRotateArray(rotateArray[1:])


s = Solution()
nums = [3, 4, 5, 1, 2]
text = s.minNumberInRotateArray(nums)
print(text)
