#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        its = [root]
        res = []
        while len(its) > 0:
            tmp = []
            new_its = []
            # print(its)
            for i in its:
                tmp.append(i.val)
                if i.left:
                    new_its.append(i.left)
                if i.right:
                    new_its.append(i.right)
            its = new_its[:]
            res.append(tmp)
        return res


# @lc code=end

