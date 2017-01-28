# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        24. Swap Nodes in Pairs
        :type head: ListNode
        :rtype: ListNode
        """
        res = cur = ListNode(0)
        cur.next = head

        while cur.next and cur.next.next:
            a = cur.next
            b = cur.next.next
            tmp = b.next
            cur.next, b.next, a.next = b, a, tmp
            cur = a

        return res.next