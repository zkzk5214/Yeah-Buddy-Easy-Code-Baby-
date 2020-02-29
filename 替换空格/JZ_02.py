class Solution(object):
    def replaceSpace(self, s):
        """
        :param s: string
        :return:string
        """
        return s.replace(' ', '%20')


s = Solution()
text = s.replaceSpace('We Are Happy.')
print(text)
