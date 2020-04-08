class Solution:
    def reverse(self, x):
        """
        :param x:int
        :return: int
        """

        num = 0
        flag = 1
        if x > 0:
            flag = 1
        else:
            flag = -1
        while x != 0:
            # num1 = 0, y1 = -465
            # num2 = -5, y2 = -46
            # num3 = -56, y3 = -4
            # num4 = -564, y4 = 0
            num = num * 10 + x % (10 * flag)
            x = int(x / 10)

        if num > 2 ** 31 - 1 or num < -2 ** 31:
            return 0
        else:
            return num


s = Solution()
x = 120
y = -465
print(s.reverse(x))
print(s.reverse(y))
