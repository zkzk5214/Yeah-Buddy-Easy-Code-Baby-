class Solution:
    def reverse(self, x):
        """
        :param x: int
        :return: int
        """

        flag = 1
        x_1 = 0

        if x < 0:
            flag = -1
            # [::-1] reverse the string
            x = int(str(abs(x))[::-1])
            # < 0
            x_1 = x * flag
        else:
            flag = 1
            x = int(str(x)[::-1])
            x_1 = x * flag

        # Only store integers within the 32-bit signed integer range:[-2^31,2^31-1]
        if x_1 > 2 ** 31 - 1 or x_1 < -2 ** 31:
            return 0
        else:
            return x_1


s = Solution()
x = 123
y = -456

print(s.reverse(x))
print(s.reverse(y))
