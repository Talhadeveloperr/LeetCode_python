# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        result = []
        while current:
            result.append(current.val)
            if current.val < -100 or current.val > 100:
                return False
            current = current.next
        if len(result) < 0 or len(result) > 300 :
            return False
        result = sorted(list(set(result)))
        dummy = ListNode(0)
        current = dummy
        for val in result:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
        