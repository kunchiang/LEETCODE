#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
from typing import List
# @lc code=start
class Solution:
    """Solution
    思路：
        一个指针i从倒数第二位开始遍历：
            if nums[i] 小于 nums[i+1:]中的最大值：
                找到nums[i+1:]中比nums[i]大一级的📚，与nums[i]交换，
                然后nums[i+1:]从小到大排序即可，return
            否则：
                i -= 1
        如果遍历了整个列表都没有返回（都是否则中的情况）：那么对整个列表进行从小到大排序即可
    """
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def sort(alist):
            if len(alist) == 1:
                return alist
            for i in range(len(alist)):
                min_ind = i
                for j in range(i, len(alist)):
                    if alist[j] <= alist[min_ind]:
                        min_ind = j
                alist[i], alist[min_ind] = alist[min_ind], alist[i]
            return alist

        def find_just_bigger(target, alist):
            for i in range(len(alist)):
                if alist[i] > target:
                    break
            # print(alist[i])
            return i

        n = len(nums)
        for i in range(n-1)[::-1]:
            tmp = max(nums[i+1:])
            if nums[i] >= tmp:
                continue
            else:
                # print(i, nums[i+1:], sort(nums[i+1:]))
                nums[i+1:] = sort(nums[i+1:])
                exind = i + 1 + find_just_bigger(nums[i], nums[i+1:])
                ex = nums[exind]
                nums[exind] = nums[i]
                nums[i] = ex
                return
        nums = sort(nums)

# sol = Solution()
# nums = [3,2,1]
# sol.nextPermutation(nums)
# print(nums)
# @lc code=end

