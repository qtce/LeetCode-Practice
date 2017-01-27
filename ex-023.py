# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    23. Merge k Sorted Lists
    """
    def mergeTwoLists(self, l1, l2):

        res = cur = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2

        return res.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []

        c = []

        for item in lists:
            c = self.mergeTwoLists(c, item)

        return c