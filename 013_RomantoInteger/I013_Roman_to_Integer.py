def getNum(x):  # Use to take the corresponding value
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
    def romanToint1(self, s):
        Num = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += Num[char]
        return number

    def romanToint2(self, s):
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


if __name__ == "__main__":
    s = Solution()
    string = s.romanToint1("MCMXCIV")
    print(string)

    # v = getNum("V")
    # print(v)
