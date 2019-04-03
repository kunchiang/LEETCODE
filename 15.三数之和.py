#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (21.18%)
# Total Accepted:    40.4K
# Total Submissions: 188.9K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution:
    def threeSum(self, nums):
        nums_sorted = sorted(nums)
        # print(nums_sorted)
        res = list()
        ex = set()
        for i in range(len(nums_sorted)):
            f = nums_sorted[i]
            for j in range(i+1, len(nums_sorted)):
                s = nums_sorted[j]
                if (f,s) in ex or (s,f) in ex:
                    continue
                for k in range(len(nums_sorted)-1, j, -1):
                    t = nums_sorted[k]
                    if f+s+t < 0:
                        break
                    if f+s+t == 0:
                        if sorted([f,s,t]) not in res:
                            res.append(sorted([f,s,t]))
                            ex.add((f,s))
                            ex.add((f,t))
        return res

sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(sol.threeSum(nums))

