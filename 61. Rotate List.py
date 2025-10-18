# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        # Convert linked list to array
        current = head
        result = []
        while current:
            result.append(current.val)
            if current.val < -100 or current.val > 100:
                return False
            current = current.next

        if len(result) < 1 or len(result) > 500 or k < 0 or k > 2 * (10**9):
            return False

        n = len(result)
        k %= n  
        if k == 0:
            return head

      
        result = result[-k:] + result[:-k]

   
        dummy = ListNode(0)
        current = dummy
        for val in result:
            current.next = ListNode(val)
            current = current.next

        return dummy.next
