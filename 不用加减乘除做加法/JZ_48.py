# -*- coding:utf-8 -*-
class Solution:
    def Add1(self, num1, num2):
        # write code here
        return sum([num1, num2])

    def Add2(self, num1, num2):
        # write code here
        # 使用位运算
        # 两个数相加可以看成两个数的每个位先相加，但不进位，然后在加上进位的数值
        # 如12+8可以看成1+0=1 2+8=0，由于2+8有进位，所以结果就是10+10=20
        # 二进制中可以表示为1000+1100 先每个位置相加不进位，
        # 则0+0=0 0+1=1 1+0=1 1+1=0这个就是按位异或运算
        # 对于1+1出现进位，我们可以使用按位与运算然后在将结果左移一位
        # 最后将上面两步的结果相加，相加的时候依然要考虑进位的情况，直到不产生进位
        # 注意python没有无符号右移操作，所以需要越界检查

        while num2:
            result = (num1 ^ num2) & 0xffffffff
            # 按位异或运算：相同位不同则为1，相同则为0。
            carry = ((num1 & num2) << 1) & 0xffffffff
            # 按位与运算：相同位的两个数字都为1，则为1；若有一个不为1，则为0。
            num1 = result
            num2 = carry
        if num1 <= 0x7fffffff:
            result = num1
        else:
            result = ~(num1 ^ 0xffffffff)
            # 在Python内部对整数的处理分为普通整数和长整数，普通整数长度为机器位长，通常都是32位，
            # 超过这个范围的整数就自动当长整数处理，而长整数的范围几乎完全没限制。
            # 当-1 + -6 通过while中的位运算操作之后，输出的计算结果是4294967289。
            # 经过~(num1^0xffffffff)这个操作会被作为负数解释输出，~运算符除了求反，还是二进制的补运算符，运算过后的二进制数字按照补码解释。
            # 就可以输出负数了。
        return result
