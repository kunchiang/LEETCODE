# 给定一个可包含重复数字的序列，返回所有不重复的全排列。 
# 
#  示例: 
# 
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ] 
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            res_list = []
            for i in nums:
                rest_nums = nums[:]
                rest_nums.remove(i)
                tmp = self.permuteUnique(rest_nums)
                for m in tmp:
                    to_add = [i] + m
                    if to_add not in res_list:
                        res_list.append(to_add)
            return res_list
# leetcode submit region end(Prohibit modification and deletion)

# sol = Solution()
# print(sol.permuteUnique([1, 1, 2]))