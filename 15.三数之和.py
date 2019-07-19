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
        n = len(nums)
        if n <= 2:
            return []
        nums_sorted = sorted(nums)
        # print(nums_sorted)
        res = list()
        if nums_sorted[0]*nums_sorted[-1] > 0:
            return []
        # 统计每个数字出现的次数
        count_dic = {}
        for i in nums:
            if i in count_dic:
                count_dic[i] += 1
            else:
                count_dic[i] = 1
        for i in range(n):
            f = nums_sorted[i]
            # 最小的数肯定不能大于零
            if f > 0:
                break
            # 当最小的这个数已经匹配过，跳过
            if i >= 1 and f == nums_sorted[i-1]:
                continue
            for j in range(i+1, n-1):
                s = nums_sorted[j]
                t = 0-f-s
                # 需要的第三个数比最后一个数大
                if t > nums_sorted[-1]:
                    continue
                # 需要的第三个数不能比第二个数还小
                if t < s:
                    continue
                # 若第二个数已经匹配过，跳过
                if j >= i+2 and s == nums_sorted[j-1]:
                    continue
                # 第三个数是否在后面的数字中
                # 线性搜索，超时
                # if t in nums_sorted[j+1:]:
                #     res.append(sorted([f,s,t]))
                # print(f, s, t)
                # 哈希搜索
                isin = False
                if t in count_dic:
                    if t == s and t != f and count_dic[t] >= 2:
                        # -2, 1, 1
                        isin = True
                    elif t == s and t == f and count_dic[t] >= 3:
                        # 0, 0, 0
                        isin = True
                    elif t != s and t != f:
                        # -2, 0, 2
                        isin = True
                if isin:
                    res.append(sorted([f,s,t]))
        return res

    def threeSum_old(self, nums):
        # 暴力搜索，超时
        nums_sorted = sorted(nums)
        # print(nums_sorted)
        res = list()
        ex = set()
        for i in range(len(nums_sorted)):
            f = nums_sorted[i]
            if f > 0:
                break
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
nums = [-1, 0, 1, 2, -1, -4, 0, 0]
# nums = [-1, 0, 1, -2, 1, 5, 0, 0, -3, 2]
# nums = [1,2,-2,-1]
# nums = [1,-1,-1,0]
# nums = [-1,0,1,0]
print(sol.threeSum(nums))
print(sol.threeSum_old(nums))

