# -*- coding:utf-8 -*-

class Solution:
    def Power(self, base, exponent):
        # write code here
        return pow(base, exponent)


# pow() Parameters
# The pow() function takes three parameters:
#
# x - a number, the base
# y - a number, the exponent
# z (optional) - a number, used for modulus
# pow(x,y,z) is equal to x^y % z

s = Solution()
text = s.Power(50, -0.000000000001)
print(text)
