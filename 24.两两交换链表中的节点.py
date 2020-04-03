#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        p = head
        q = p.next
        # 第一次交换 p, q
        p.next = q.next
        q.next = p
        # 头结点的指向改变了
        head = q
        # 如果后面还有节点，继续交换
        while p.next:
            s = p # 相当于”头结点“，需要保持"头结点"的指向为更换后的下一个节点
            p = p.next
            if p.next:
                q = p.next
            else:
                break
            # exchange p, q
            p.next = q.next
            q.next = p
            # 保持"头结点"的指向为更换后的下一个节点
            s.next = q
        return head

# @lc code=end

