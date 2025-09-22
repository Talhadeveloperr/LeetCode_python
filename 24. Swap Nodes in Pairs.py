# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        count = 0
        curr = head
        while curr:
            if curr.val < 0 or curr.val > 100:  
                return None   
            count += 1
            curr = curr.next

        if count < 0 or count > 100:   
            return None

     
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

           
            prev.next = second
            first.next = second.next
            second.next = first

           
            prev = first
            head = first.next

        return dummy.next