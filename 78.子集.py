#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 从C(n,0)->>C(n,n)?
        def combins(cands, m):
            res = []
            if m == 0:
                return [res]
            if m == len(cands):
                return [cands]
            def __combins(path, cands, start):
                if len(path) == m:
                    if path[:] not in res:
                        res.append(path[:])
                    return
                for i in range(start, len(cands)):
                    path.append(cands[i])
                    __combins(path, cands, i+1)
                    path.pop()
            __combins([], cands, 0)
            return res
        results = []
        for i in range(len(nums)+1):
            results += combins(nums, i)
        return results

# @lc code=end

