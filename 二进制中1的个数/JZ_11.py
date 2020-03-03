class Solution(object):
    def Number0f1(self, n):
        """
        :param n: int
        :return: int
        """
        count = 0
        if n < 0:
            n = n * 0xffffffff  # negative plus -1
        while n:
            count += 1
            n = n & (n - 1)
        return count


s = Solution()
result = s.Number0f1(6)  # 110
print(result)

# 110 & 101 = 100
# 100 & 011 = 000
# count 2
