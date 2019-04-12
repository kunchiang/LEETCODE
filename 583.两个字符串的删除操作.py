#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#
# https://leetcode-cn.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (41.17%)
# Total Accepted:    842
# Total Submissions: 2.1K
# Testcase Example:  '"sea"\n"eat"'
#
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
# 
# 示例 1:
# 
# 
# 输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
# 
# 
# 说明:
# 
# 
# 给定单词的长度不超过500。
# 给定单词中的字符只含有小写字母。
# 
# 
#
class Solution:
    def minDistance(self, word1, word2):
        # 当某个单词为空，直接返回另一个单词的长度
        if not word1 or not word2:
            return max(len(word1), len(word2))
        m = len(word1)
        n = len(word2)
        # dp[i][j]表示word1[0,...,i-1]和word2[0,...,j-1]的最长公共子序列长度
        # dp = [[0]*(n+1)]*(m+1) : 这是错误的初始化方式！！
        # # np.zeros((m+1,n+1))
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        # 动态规划
        for i in range(1, m+1):
            # count = 0
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    # print("i:{}, j:{}, char:{}".format(i-1,j-1,word1[i-1]))
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        # print(dp[m][n])
        return int(m+n-2*dp[m][n])


# w1 = "inte"
# w2 = "exe"

# sol = Solution()
# res = sol.minDistance(w1, w2)
# print(res)

