class Solution:
    def isPalindrome(self, x):
        """
        :param x: int
        :return: bool
        """
        if x < 0:  # Negative Numbers are not palindrome
            return False
        elif x != int(str(x)[::-1]):  # Number turn to str, reverse then turn back to int
            return False
        else:
            return True


#  [::-1]make a copy of the same list in reverse order

s = Solution()
S = s.isPalindrome(1234321)
print(S)
