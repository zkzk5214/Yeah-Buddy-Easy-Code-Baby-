class Solution:
    def jumpFloorII(self, n):
        return 2 ** (n - 1)


s = Solution()
result = s.jumpFloorII(4)
print(result)

# f(n)=2^(n-1)
