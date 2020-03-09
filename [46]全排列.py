# 给定一个没有重复数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    """
    思路：如[1,2,3]，要获得[1,2,3]的全排列，
        就需要获得：1 + [[2,3]的全排列]；2 + [[1,3]的全排列]；3 + [[1,2]的全排列]
        即，递归体为：
        for i in nums:
            获取除i之外的全排列
            将i与上面的结果拼接起来
        同理[2,3]的全排列等于：2+[3] 和 3+[2]
    """

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 递归出口
        if len(nums) <= 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            res_list = []
            for i in nums:
                # 当前数字为i
                rest_nums = nums[:]
                rest_nums.remove(i)
                # 递归获取除了i之外的其他数字的全排列
                tmp = self.permute(rest_nums)
                # 将除了i之外的其他数字的全排列的结果与i拼接
                for m in tmp:
                    res_list.append([i] + m)
            return res_list

# sol = Solution()
# print(sol.permute([1, 2, 3, 4]))
# leetcode submit region end(Prohibit modification and deletion)
