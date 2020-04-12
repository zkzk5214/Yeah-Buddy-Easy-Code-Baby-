import os.path as op


class Solution(object):
    def longestCommonPrefix1(self, strs):
        """
        :param strs: List[str]
        :return: str
        """
        return op.commonprefix(strs)
        # Return the longest path prefix (taken character-by-character)
        # that is a prefix of all paths in list.
        # If list is empty, return the empty string ('').

    def longestCommonPrefix2(self, strs):
        """
        :param strs: List[str]
        :return: str
        Create an list for strs
        Eg: ['abc', 'abb', 'abc']
        strs[0][0]= a
        """
        # Minimal length of strs
        minL = min(map(len, strs)) if strs else 0
        for i in range(minL):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    print(strs)
                    return strs[0][:i]
        return strs[0][:minL] if minL else ""


if __name__ == "__main__":
    s = Solution()
    string = s.longestCommonPrefix2(['abc', 'abb', 'abc'])
    print(string)
