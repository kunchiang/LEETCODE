#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (54.76%)
# Total Accepted:    38.3K
# Total Submissions: 69.8K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 
# 说明：你不能倾斜容器，且 n 的值至少为 2。
# 
# 
# 
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
# 
# 
# 
# 示例:
# 
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
# 
#
class Solution:
    def maxArea(self, height):
        # import time
        # st = time.time()
        n = len(height)
        res = 0
        i = 0
        j = n-1
        while i<j:
            tmp = (j - i)*min(height[i], height[j])
            res = max(res, tmp)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        '''
        # 暴力搜索，超时
        for i in range(n):
            if i > 0 and height[i] < height[i-1]:
                continue
            for j in range(n-1, i, -1):
                if j < n-1 and height[j] < height[j+1]:
                    continue
                tmp = (j - i)*min(height[i], height[j])
                if tmp > res:
                    res = tmp
        '''
        # print("[+] Cost time: ", time.time()-st)
        return res

# height = [1,2]
# sol = Solution()
# print(sol.maxArea(height))

