#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
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
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        if k == 1:
            return [[i] for i in range(1, n+1)]
        if k == n:
            return [list(range(1, n+1))]
        # print(cands)
        result = []
        ## 超时
        # cands = list(range(1, n+1))
        # def backtrack(path, cands):
        #     # print(path)
        #     if len(path) == k:
        #         # res = sorted(path[:])
        #         if path[:] not in result:
        #             result.append(path[:])
        #         return
        #     for i in range(len(cands)):
        #         c = cands[i]
        #         path.append(c)
        #         cands.pop(i)
        #         backtrack(path, cands)
        #         cands.insert(i, c)
        #         path.pop()

        def backtrack2(path, first):
            if len(path) == k:
                result.append(path[:])
            for i in range(first, n+1):
                path.append(i)
                backtrack2(path, i+1)
                path.pop()
        # backtrack([], cands)
        backtrack2([], 1)
        return result

# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.combine(13, 10))

# @lc code=end

