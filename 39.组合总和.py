#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from typing import List
# @lc code=start
class Solution:
    """dfs模板
    result = []
    def backtrack(路径, 选择列表):
        if 满足结束条件:
            result.add(路径)
            return
        for 选择 in 选择列表:
            做选择
            backtrack(路径, 选择列表)
            撤销选择
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        n = len(candidates)
        if n == 0:
            return result
        sort_cands = sorted(candidates)
        def backtracking(picked, idx, target):
            if target == 0:
                # print(idx, picked)
                result.append(picked[:])
                return
            for i in range(idx, n):
                # print(idx, i, target, sort_cands[i], picked)
                red = target - sort_cands[i]
                if red < 0:
                    break
                picked.append(sort_cands[i])
                backtracking(picked, i, red)
                picked.pop()
        backtracking([], 0, target)
        return result

# if __name__ == "__main__":
#     sol = Solution()
#     candidates = [2,3,5]
#     target = 8
#     print(sol.combinationSum(candidates, target))

# @lc code=end

