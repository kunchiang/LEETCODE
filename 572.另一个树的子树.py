#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def issub(self, s, t):
        if s != None and t != None:
            return s.val == t.val and self.issub(s.left, t.left) and self.issub(s.right, t.right)
        return s is t

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None:
            return False
        if self.issub(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


