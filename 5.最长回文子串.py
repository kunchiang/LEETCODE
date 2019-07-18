#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
class Solution:
    def longestPalindrome(self, s):
        ls = len(s)
        if ls <= 1:
            return s
        # 双端扩展，对于每一个点都展开双端扩展，直到双端不等为止
        res = ''
        for i in range(ls):
            j, k = i, i
            tmp = s[j:k+1]
            while j>=0 and k<ls and s[j] == s[k]:
                tmp = s[j:k+1]
                j -= 1
                k += 1
            if len(tmp)>len(res):
                res = tmp

            if i+1<ls and s[i] != s[i+1]:
                continue
            j, k = i, i+1
            tmp = s[j:k+1]
            while j>=0 and k<ls and s[j] == s[k]:
                tmp = s[j:k+1]
                j -= 1
                k += 1
            if len(tmp)>len(res):
                res = tmp
        return res


sol = Solution()
s = "baabad"
print(sol.longestPalindrome(s))


