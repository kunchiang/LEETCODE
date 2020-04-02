#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 最简单最暴力，一行代码解决问题：
        return sorted(list(nums))[-k]

# @lc code=end

