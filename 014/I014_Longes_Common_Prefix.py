import os.path as op


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :param strs: List[str]
        :return: str
        """
        return op.commonprefix(strs)
        # Return the longest path prefix (taken character-by-character) that is a prefix of all paths in list.
        # If list is empty, return the empty string ('').


s = Solution()
string = s.longestCommonPrefix(['abc', 'abb', 'abc'])
print(string)
