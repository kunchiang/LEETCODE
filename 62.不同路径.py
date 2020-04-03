#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    """动态规划
    状态转移方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
        且 dp[1][1] = 1
    """
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    """数学问题
        m+n-2个选择中选择m-1个（或n-1个）
    """
    def uniquePaths2(self, m: int, n: int) -> int:
        import math
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))

sol = Solution()
print(sol.uniquePaths(7, 3))
print(sol.uniquePaths2(7, 3))

# @lc code=end

