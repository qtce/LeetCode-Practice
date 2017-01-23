# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    21. Merge Two Sorted Lists
    """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = l1
        c1 = l1
        c2 = l2
        if l1 == None and l2 == None:
            return []
        elif l1 == None:
            return l2
        else:
            return l1

        temp1 = c1.next
        temp2 = c2.next

        while c1.next != None or c2.next != None:
            if c1.val <= c2.val and c1.next.val > c2.val:
                temp1 = c1.next
                temp2 = c2.next
                c1.next = c2
                c1.next.next = temp1
                c1 = temp1
                c2 = temp2
            elif c1.val < c2.val and c1.next.val <= c2.val:
                c1 = c1.next
            else:
                temp2 = c2.next
                temp1 = c1
                c1 = c2
                c1.next = temp1
                c2 = temp2

        return c1