class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        self.DFS(candidates, target, 0, res, [])
        return res

    def DFS(self, candidates, target, start, res, intermedia):
        if target == 0:
            res.append(intermedia)
            return
        for i in range(start, len(candidates)):
            # range(0,4)
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i, res, intermedia + [candidates[i]])


# 1.0
# i=0 , 7>candidates[0]=2, candidates=[2, 3, 6, 7]
# 1.1
# target - candidates[0]=5, i = 0, res = [], intermedia = intermedia + [candidates[i]] = [2]
# 1.2
# target - candidates[0]=3, i = 0, res = [], intermedia = [2, 2]
# 1.3
# target - candidates[0]=1, target=1 < candidates[0]
# 1.4
# i = 1, target = 3
# target - candidates[1]=0, i = 1, res = [], intermedia = intermedia + [candidates[1]] = [2,2,3]
# 1.5
# target = 0, res = [intermedia] = [[2,2,3]]

s = Solution()
candidates = [2, 3, 6, 7]
test = s.combinationSum(candidates, target=7)
print(test)
