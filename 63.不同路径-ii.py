#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ## 牛皮！实在想不到。。。@语法糖有点甜
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [1] + [0]*n
        for i in range(0,m):
            for j in range(0,n):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j]+dp[j-1]
        return dp[-2]
        # if obstacleGrid[0][0] == 1:
        #     return 0
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[-1])
        # dp = [[1 for i in range(n)] for j in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if obstacleGrid[i-1][j] == 1:
        #             dp[i-1][j] = 0
        #             dp[i][j] = dp[i][j-1]
        #         elif obstacleGrid[i][j-1] == 1:
        #             dp[i][j-1] = 0
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[-1][-1]
# @lc code=end

