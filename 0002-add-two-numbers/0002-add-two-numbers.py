# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode=ListNode(-1)
        head=dummynode
        temp1=l1
        temp2=l2
        carry=0
        while temp1!=None or temp2!=None:
            summ=carry
            if temp1:
                summ+=temp1.val
                temp1=temp1.next
            if temp2:
                summ+=temp2.val
                temp2=temp2.next
            carry=summ//10
            newnode=ListNode(summ%10)
            dummynode.next=newnode
            dummynode=newnode
        if carry!=0:
            newnode=ListNode(carry)
            dummynode.next=newnode
            dummynode=newnode
        return head.next
        

        