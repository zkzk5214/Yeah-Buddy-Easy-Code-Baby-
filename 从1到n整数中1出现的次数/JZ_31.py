# -*- coding:utf-8 -*-
class Solution:
    def Counting1(self, n):
        # write code here
        count = 0
        for i in range(1, n + 1):
            for j in str(i):
                if j == '1':
                    count += 1
        return count

    def Counting2(self, n):
        # write code here
        count = 0
        for i in range(0, n + 1):
            temp = i
            while temp:
                if temp % 10 == 1:
                    count += 1
                temp /= 10
        return count


s = Solution()
text = s.Counting1(n=10)  # 1,10
print(text)
