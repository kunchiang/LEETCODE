#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (25.55%)
# Total Accepted:    8.4K
# Total Submissions: 32.1K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 
# 示例 1:
# 
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
# 
# 示例 2:
# 
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# 
#
class Solution:

    def longestValidParentheses(self, s):
        n = len(s)
        if n <= 1:
            return 0
        dp = [0]*(n)
        stack = []
        gap = 0
        count = 0
        sp = True
        if s[0] == '(':
            stack.append('(')
        for i in range(1, n):
            if s[i] == '(':
                stack.append(s[i])
                dp[i] = dp[i-1]
                if dp[i] > 0 and not sp:
                    gap += 1
                    count = 0
                sp = False
            else:
                if len(stack) == 0:
                    dp[i] = dp[i-1]
                    sp = True
                    gap = 0
                else:
                    if gap == 0:
                        dp[i] = dp[i-1] + 1
                    else:
                        count += 1
                        gap -= 1
                        if gap == 0:
                            dp[i] = dp[i-1]+count
                        else:
                            dp[i] = max(dp[i-1], count)
                    stack.pop()
        print(dp)
        return 2*dp[n-1]

sol = Solution()
# print(sol.longestValidParentheses("()"))
# assert sol.longestValidParentheses("()") == 2
# assert sol.longestValidParentheses(")()())") == 4
# assert sol.longestValidParentheses("((()(())())") == 10
# assert sol.longestValidParentheses(")))))(((()(") == 2
assert sol.longestValidParentheses("()))(())") == 4
assert sol.longestValidParentheses("()((()()") == 4
# assert sol.longestValidParentheses("())())()())") == 4


