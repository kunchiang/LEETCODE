# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。 
# 
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。 
# 
#  
# 
#  示例: 
# 
#  输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#  
# 
#  说明: 
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。 
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def pick(self, list1, list2):
        res_list = []
        for i in list1:
            for j in list2:
                res_list.append(i+j)
        return res_list

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) <= 0:
            return []
        dig_dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        res_list = dig_dict[digits[0]]
        if len(digits) == 1:
            return res_list
        for i in range(1, len(digits)):
            tmp_list = dig_dict[digits[i]]
            res_list = self.pick(res_list, tmp_list)
        return res_list

# sol = Solution()
# print(sol.letterCombinations("23"))

# leetcode submit region end(Prohibit modification and deletion)
