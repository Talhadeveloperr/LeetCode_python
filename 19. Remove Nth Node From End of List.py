# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        
        current = head
        result = []
        while current:
            result.append(current.val)
            if current.val < 0 or current.val > 100:
                return False
            current = current.next

        if len(result) < 1 or len(result) > 30:
            return False
        if n < 1 or n > len(result):  
            return False

        dummy = ListNode(0, head)
        first = second = dummy

        
        for _ in range(n+1):
            if first:     
                first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

