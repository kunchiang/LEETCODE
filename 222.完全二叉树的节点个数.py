#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        count = []
        if root == None:
            return len(count)
        p = root
        def dfs(p):
            if p == None:
                return
            if p != None:
                count.append(1)
            if p.left != None:
                dfs(p.left)
            if p.right != None:
                dfs(p.right)
        dfs(p)
        return len(count)


# @lc code=end

