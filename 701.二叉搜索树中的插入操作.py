#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 新增节点策略，不替换原有节点
        def bsinsert(node, val):
            if val < node.val:
                if node.left:
                    bsinsert(node.left, val)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    bsinsert(node.right, val)
                else:
                    node.right = TreeNode(val)
        bsinsert(root, val)
        return root


# @lc code=end

