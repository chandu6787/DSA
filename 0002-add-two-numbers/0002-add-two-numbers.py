# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dnode=ListNode(-1)
        current=dnode
        while l1!=None or l2!=None:
            summ=carry
            if l1:
                summ=summ+l1.val
            if l2:
                summ=summ+l2.val
            newNode=ListNode(summ%10)
            current.next=newNode
            current=newNode
            carry=summ//10
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry:
            newNode=ListNode(carry)
            current.next=newNode
            current=newNode

        return dnode.next
            
            
        