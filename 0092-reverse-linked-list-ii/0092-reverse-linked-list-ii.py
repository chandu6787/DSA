# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p=0
        temp=head
        stack=[]
        while temp!=None:
            p+=1
            if p>=left and p<=right:
                stack.append(temp.val)
            temp=temp.next
        p=0
        temp=head
        while temp!=None:
            p+=1
            if p>=left and p<=right:
                temp.val=stack[-1]
                stack.pop()
            temp=temp.next
        return head


        