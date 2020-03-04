class Solution(object):
    def jumpFloor(self, n):
        res = [1, 2]
        while len(res) <= n:
            res.append(res[-1] + res[-2])
        if n == 1:
            return 1
        else:
            return res[n - 1]


s = Solution()
result = s.jumpFloor(4)
print(result)

#        | 1, (n=1)
# f(n) = | 2, (n=2)
#        | f(n-1)+f(n-2) ,(n>2)
