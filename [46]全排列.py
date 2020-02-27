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

    def permute(self, nums):
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
            # print(nums)
            for i in nums:
                rest_nums = nums[:]
                rest_nums.remove(i)
                tmp = self.permute(rest_nums)
                # print("tmp: ", tmp)
                for m in tmp:
                    if isinstance(m, list):
                        res_list.append([i] + m)
                    else:
                        res_list.append([i, m])
                    # print("[+]", [i, m])
                # res_list.append([i, self.permute(rest_nums)])
            return res_list

# sol = Solution()
# print(sol.permute([1, 2, 3, 4]))
# leetcode submit region end(Prohibit modification and deletion)
