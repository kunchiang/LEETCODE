#
# @lc app=leetcode.cn id=958 lang=python3
#
# [958] 二叉树的完全性检验
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    层次遍历方法：需要考虑的就是当出现了空节点之后，后面不能再出现非空节点
    因此设置一个flg，初始化为False，当遇到空节点就设置为True
    层次遍历过程中，如果出现了flg=True且当前节点不为空时，就可以确定不完全二叉树了
    """
    def isCompleteTree(self, root: TreeNode) -> bool:
        # def dfs(node):
        #     if node:
        #         if node.right and not node.left:
        #             return False
        #         else:
        #             return True and dfs(node.left) and dfs(node.right)
        #     else:
        #         return True
        # return dfs(root)

        # 层次遍历
        level = [root]
        # 遍历当前层
        flg = False # 记录前面的节点是否有空节点
        while len(level) > 0:
            next_level = []
            for i in range(len(level)):
                node = level[i]
                # 如果当前节点为空，标记flg也会转换成True
                if not node:
                    flg = True
                    continue
                # 当当前节点不为空，且flg为True，
                # 说明出现了当前层存在“右边不为空时左边节点为空”的情况，
                # 也就是该层不符合完全二叉树的性质
                if node and flg:
                    return False
                # 当前节点的左孩子不存在而右孩子存在，不符合完全二叉树性质
                if node.right and not node.left:
                    return False
                # 按从左至右的顺序添加下一层的所有节点
                next_level.append(node.left)
                next_level.append(node.right)
            level = next_level[:]
        return True


# @lc code=end

