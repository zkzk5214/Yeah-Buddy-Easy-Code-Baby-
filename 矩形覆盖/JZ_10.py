class Solution(object):
    def rectCover(self, number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            res = [0, 1, 2]
            while len(res) <= number:
                res.append(res[-1] + res[-2])
            else:
                return res[number]


s = Solution()
result = s.rectCover(3)
print(result)
