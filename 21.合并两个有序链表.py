#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (52.91%)
# Total Accepted:    49.9K
# Total Submissions: 94K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            reslist = l1
            p = reslist
            l1 = l1.next
        else:
            reslist = l2
            p = reslist
            l2 = l2.next
        while True:
            if l1 == None:
                p.next = l2
                break
            if l2 == None:
                p.next = l1
                break
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            elif l2.val < l1.val:
                p.next = l2
                l2 = l2.next
                p = p.next
            else:
                p.next = l1
                l1 = l1.next
                p = p.next
                p.next = l2
                l2 = l2.next
                p = p.next

        return reslist

# l1 = ListNode(0)
# p = l1
# p.next = ListNode(6)
# p = p.next
# p.next = ListNode(7)
# p = p.next

# l2 = ListNode(1)
# p = l2
# p.next = ListNode(1)
# p = p.next
# p.next = ListNode(4)
# p = p.next
# p.next = ListNode(4)
# p = p.next
# p.next = ListNode(5)
# p = p.next

# sol = Solution()

# res = sol.mergeTwoLists(l1,l2)
# q = res
# while q!=None:
#     print(q.val)
#     q = q.next

