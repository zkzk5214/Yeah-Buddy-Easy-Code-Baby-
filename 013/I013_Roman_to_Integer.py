def getNum(x):      # Use to take the corresponding value
    return {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }.get(x)


class Solution:
    def romanToint(self, s):
        """
        :param s: str
        :return: int
        """
        Num = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        result = 0
        for i in range(len(s)):  # MCMXCIV = 7
            if i > 0 and Num[s[i]] > Num[s[i - 1]]:
                result = result + Num[s[i]] - 2 * Num[s[i - 1]]
                # Minus twice the previous number and then plus that number
            else:
                result += Num[s[i]]
        return result


s = Solution()
string = s.romanToint("MCMXCIV")
print(string)

v = getNum("V")
print(v)
