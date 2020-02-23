class Solution:
    def combinationSum(self, candidates, target):
        """
        :param candidates: a list of integers
        :param target: integer
        :return: a list of lists of integers
        """
        candidates.sort()
        res = set()
        # set() method is used to convert any of the iterable to the distinct element
        # and sorted sequence of iterable elements
        intermedia = []
        self.recursion(candidates, target, res, intermedia)
        return [list(i) for i in res]

    # candidates = [2,3,6,7]
    def recursion(self, candidates, target, res, intermedia):
        for i in candidates:
            if target == i:
                # 1.3
                # t=3 = i=3
                temp = intermedia + [i]
                # t = t - i = 0, intermedia = [2,2]+[3]
                temp.sort()
                if temp is not None:
                    res.add(tuple(temp))  # add the first tuple [2,2,3]
                return
            elif target > i:
                # 1.1
                # t=7 > i=2
                # 1.2
                # t=5 > i=2
                self.recursion(candidates, target - i, res, intermedia + [i])
                # t = t - i = 5, intermedia = []+[2]
                # t = t - i = 3, intermedia = [2]+[2]
            else:
                return


s = Solution()
test = s.combinationSum(candidates=[2, 3, 6, 7], target=7)
print(test)
