class Solution(object):
    def isPalindrome(self, x):
        """
        :param x: int
        :return: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            # Negative Numbers are not palindrome
            # if a number is a positive number, and it's divisible by my 0, then it's definitely not a palindrome
            return False

        rev, y = 0, x

        while x > 0:
            rev = rev * 10 + x % 10  # Get unit number and add to rev
            x /= 10  # Shrink x
            return y == rev


s = Solution()
S = s.isPalindrome(123)
print(S)
