#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
from typing import List

# @lc code=start
class Solution:
    def _generateParenthesis(self, n: int) -> List[str]:
        res = []
        currStr = ''
        def dfs(currStr, left, right):
            # 递归出口：
            # 出口1：正确括号序列，添加到结果集
            # 出口2：非法括号序列
            if left ==0 and right == 0:
                res.append(currStr)
                return
            elif left > right:
                # 剩下的括号中，左括号数量不能大于右括号，
                # 如“(()))"，剩下的不管怎么组肯定是非法的
                return
            # 递归放括号
            # 相当于遍历左子树
            if left > 0:
                dfs(currStr+'(', left-1, right)
            # 相当于遍历右子树
            if right > 0:
                dfs(currStr+')', left, right-1)
        dfs(currStr, n, n)
        return res
    '''
    动态规划，动态转移方程：
    dp[0] = ['']
    dp[1] = ['()']
    dp[2] = ['(())', '()()']
        dp[2][0] = '(' + dp[1] + ')' + dp[0] = '(())'
        dp[2][1] = '(' + dp[0] + ')' + dp[1] = '()()'
    .
    .
    .
    dp[i] = '(' + dp[p][...] + ')' + dp[q][...] ; p+q=i-1
    '''
    def generateParenthesis(self, n):
        if n == 0:
            return []
        dp = []
        dp.append([''])
        dp.append(['()'])
        for i in range(2, n+1):
            tmp = []
            for p in range(i)[::-1]:
                for a in dp[p]:
                    for b in dp[i-1-p]:
                        tmp.append('('+a+')'+b)
            dp.append(tmp)
        return dp[n]

# sol = Solution()
# print(sol.generateParenthesis(3))

# @lc code=end

