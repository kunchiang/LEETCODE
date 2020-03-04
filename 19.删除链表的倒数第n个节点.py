#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ## 两趟
        # tmp_list = []
        # q = head
        # while q != None:
        #     tmp_list.append(q.val)
        #     q = q.next
        # if n == len(tmp_list):
        #     return head.next
        # new_head = ListNode(tmp_list[0])
        # p = new_head
        # for t in range(1, len(tmp_list)):
        #     if t != len(tmp_list) - n:
        #         nod = ListNode(tmp_list[t])
        #         p.next = nod
        #         p = p.next
        # return new_head
        ### 一趟扫描，记住每个节点，原地修改
        ps = []
        p = head
        while p != None:
            ps.append(p)
            p = p.next
        if n == len(ps):
            return head.next
        elif n == 1:
            ps[-n-1].next = None
        else:
            ps[-n-1].next = ps[-n+1]
        return head

# @lc code=end

