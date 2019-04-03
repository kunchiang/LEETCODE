# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        ad = 0
        while l1.next != None and l2.next!=None:
            s=l1.val+l2.val+ad
            res.val = s%10
            ad = int(s/10)
            l1 = l1.next
            l2 = l2.next
            res = res.next
        return res
