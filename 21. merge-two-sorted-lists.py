# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        

        def validate_input(head):
            count = 0
            cur = head
            while cur:
                if cur.val < -100 or cur.val > 100:
                    return False
                count += 1
                if count > 50:      
                    return False
                cur = cur.next
            return True

       
        if not validate_input(list1) or not validate_input(list2):
            return None  

        dummy = ListNode(0)
        tail = dummy

        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        
        tail.next = list1 if list1 else list2

        return dummy.next