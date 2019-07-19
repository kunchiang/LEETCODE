#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        if n <= 3:
            return sum(nums)
        nums_sorted = sorted(nums)
        bsum = nums_sorted[0] + nums_sorted[1] + nums_sorted[2]
        for k in range(0, n-2):
            if k > 0 and nums_sorted[k-1] == nums_sorted[k]:
                continue
            i, j = k+1, n-1
            while i < j:
                tmp = nums_sorted[k] + nums_sorted[i] + nums_sorted[j]
                if abs(tmp - target) < abs(bsum - target):
                    bsum = tmp
                if tmp > target:
                    j -= 1
                elif tmp < target:
                    i += 1
                else:
                    # print(target)
                    return target
        # print(bsum)
        return bsum


    def threeSumClosest_old(self, nums, target):
        # 暴力搜索，超时，O(n3)
        n = len(nums)
        if n <= 3:
            return sum(nums)
        nums_sorted = sorted(nums)
        bsum = nums_sorted[0] + nums_sorted[1] + nums_sorted[2]
        for i in range(n-2):
            f = nums_sorted[i]
            for j in range(i+1, n-1):
                s = nums_sorted[j]
                for k in range(j+1, n):
                    t = nums_sorted[k]
                    tmp = f + s + t
                    if abs(tmp - target) < abs(bsum - target):
                        # print(f, s, t)
                        bsum = tmp
        print(bsum)
        return bsum



sol = Solution()
nums = [-1, 2, 1, -4]
target = 1 # 2

nums = [1,2,4,8,16,32,64,128]
target = 82 # 82

sol.threeSumClosest(nums, target)

