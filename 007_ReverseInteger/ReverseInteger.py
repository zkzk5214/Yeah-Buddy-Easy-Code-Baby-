class Solution:
    def reverse1(self, x):
        """
        :param x: int
        :return: int
        [::-1] reverse the string
        """
        if x < 0:
            output = int(str(abs(x))[::-1]) * -1
        else:
            output = int(str(x)[::-1])

        # Only store integers within the 32-bit
        # signed integer range:[-2^31,2^31-1]
        if output > 2 ** 31 - 1 or output < -2 ** 31:
            return None
        else:
            return output

    def reverse2(self, x):
        """
        :param x:int
        :return: int
        """
        num = 0
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


if __name__ == "__main__":
    s = Solution()
    x = 123
    y = -456

    print(s.reverse1(x))
    print(s.reverse2(y))
