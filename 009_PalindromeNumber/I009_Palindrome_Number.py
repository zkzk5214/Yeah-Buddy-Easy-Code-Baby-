class Solution:
    def isPalindrome1(self, x):
        """
        :param x: int
        :return: bool
        [::-1] reverse num
        """
        if x < 0:
            # Negative Numbers are not palindrome
            return False
        elif x != int(str(x)[::-1]):
            return False
        else:
            return True

    def isPalindrome2(self, x):
        """
        :param x: int
        :return: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            # Negative Numbers are not palindrome
            # If a number is a positive number,
            # and it's divisible by my 0,
            # then it's definitely not a palindrome
            return False

        num, y = 0, x

        while x > 0:
            # Get the remainder, add to num
            num = num * 10 + x % 10
            x /= 10
            return y == num


if __name__ == "__main__":
    s = Solution()
    S = s.isPalindrome1(1234321)
    print(S)
