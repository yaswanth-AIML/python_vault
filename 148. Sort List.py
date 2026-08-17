# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li=[]
        curr=head
        while curr:
            li.append(curr.val)
            curr=curr.next
        li.sort()
        curr=head
        for i in li:
            curr.val=i
            curr=curr.next
        return head
         
