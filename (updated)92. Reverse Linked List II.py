# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        li=[]
        curr=head
        i=1
        while curr:
            if i>=left and i<=right:
                li.append(curr.val)
            i+=1
            curr=curr.next
        li.reverse()
        curr=head
        i=1
        k=0
        while curr:
            if i>=left and i<=right:
                curr.val=li[k]
                k+=1
            i+=1
            curr=curr.next
        return head 
