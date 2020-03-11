# -*- coding:utf-8 -*-
class Solution(object):
    def Sum_Solution(self, n):
        # write code here
        return sum(list(range(1, n + 1)))


# list(range(1, n+1)) [1,2,3,...,n]
s = Solution()
n = 5
text1 = s.Sum_Solution(n)
print(text1)
