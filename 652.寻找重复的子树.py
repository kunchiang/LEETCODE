#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """根据官方解答做出的。。。
        思路是递归的为每个子树创建计数字典，计数值大于1就是重复子树
        字典形如：{node1.uid: count1, node2.uid: count2}
            其中node1.uid = (node1.val, node1.leftchild.uid, node1.rightchild.uid)
    """
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        count = dict()
        res = []
        def lookup(node):
            if node:
                uid = (node.val, lookup(node.left), lookup(node.right))
                if uid not in count:
                    count[uid] = 1
                else:
                    count[uid] += 1
                if count[uid] == 2:
                    res.append(node)
                return uid
        lookup(root)
        return res


# @lc code=end

