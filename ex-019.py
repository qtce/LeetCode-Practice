# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        19. Remove Nth Node From End of List
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res = []
        item = head

        while item.next != None:
            res.append(item.val)
            item = item.next

        res.append(item.val)
        del res[len(res) - n]

        return res