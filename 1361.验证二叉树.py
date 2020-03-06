#
# @lc app=leetcode.cn id=1361 lang=python3
#
# [1361] 验证二叉树
#

# @lc code=start
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        mark = [0 for i in range(n)]
        for i in range(len(leftChild)):
            if leftChild[i] == 0 or rightChild[i] == 0:
                return False
            else:
                if leftChild[i] != -1:
                    mark[leftChild[i]] += 1
                if rightChild[i] != -1:
                    mark[rightChild[i]] += 1
        for j in mark[1:]:
            if j != 1:
                return False
        return True

# sol = Solution()
# n = 4
# leftChild = [1,-1,3,-1]
# rightChild = [2,-1,-1,-1]
# print(sol.validateBinaryTreeNodes(n, leftChild, rightChild))

# @lc code=end

