class Solution(object):
    def reOrderArray1(self, array):
        # write code here
        odd, even = [], []
        for i in array:
            odd.append(i) if i % 2 == 1 else even.append(i)
        return odd + even

    def reOrderArray2(self, array):
        return sorted(array, key=lambda c: c % 2, reverse=True)
    # 奇数%2 == 1 偶数%2 == 0
    # reverse=True --> 奇数排偶数前面


s = Solution()
nums = [3, 4, 5, 1, 2]
text1 = s.reOrderArray1(nums)
print(text1)
text2 = s.reOrderArray2(nums)
print(text2)
