#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        if len(candidates) == 0:
            return result
        def dfs(picked, i, target, candidates):
            if target == 0:
                res = sorted(picked[:])
                if res not in result:
                    result.append(res)
                return
            for j in range(i, len(candidates)):
                tmp = candidates[j]
                rest = target - tmp
                if rest < 0:
                    break
                # 这是一个候选集会修改的问题
                # 添加新的选后，还需要在候选集中删除对应元素
                # 相应的，在回溯的过程中也要恢复候选集
                picked.append(tmp)
                candidates.pop(j)
                dfs(picked, j, rest, candidates)
                picked.pop()
                candidates.insert(j, tmp)
        dfs([], 0, target, sorted(candidates))
        return result

# if __name__ == "__main__":
#     sol = Solution()
#     candidates = [10,1,2,7,6,1,5]
#     target = 8
#     print(sol.combinationSum2(candidates, target))

# @lc code=end

