# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        25. Reverse Nodes in k-Group
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        h = pre = ListNode(0)
        h.next = cur = pre.next = head
        count, c = 1, 1

        if not head or not head.next: return head

        while cur.next:
            count += 1
            cur = cur.next

        if count < k: return head

        cur, count = head, 1

        while cur and cur.next:
            while cur and cur.next and c < k:
                tmp1 = cur.next.next
                tmp2 = pre.next
                pre.next = cur.next
                cur.next = tmp1
                pre.next.next = tmp2
                c += 1

            pre, cur, c = cur, cur.next, 1

            if not cur: break
            while cur.next:
                count += 1
                cur = cur.next
            if count < k: break

            cur, count = pre.next, 1

        return h.next