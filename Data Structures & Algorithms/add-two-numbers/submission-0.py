# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
         1000 [0,0,0,1]
        +0001 [1]
        =1001 [1,0,0,1]
        dummy = curr = ListNode()
        carry = 0
        while l1 or l2:
            a = 0 if l1 is None else l1.val
            b = 0 if l2 is None else l2.val
            res = carry + a + b
            carry = 0
            if res > 9:
                carry = 1
                res = res - 10
            curr.next = ListNode(res)
            curr = curr.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return dummy.next
        '''

        dummy = curr = ListNode()
        carry = 0
        while l1 or l2:
            a = 0 if l1 is None else l1.val
            b = 0 if l2 is None else l2.val
            res = carry + a + b
            carry = 0
            if res > 9:
                carry = 1
                res = res - 10
            curr.next = ListNode(res)
            curr = curr.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry == 1:
            curr.next = ListNode(carry)
        return dummy.next
            

