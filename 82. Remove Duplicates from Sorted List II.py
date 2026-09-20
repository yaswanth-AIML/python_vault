# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        li={}
        while curr:
            li[curr.val]=li.get(curr.val, 0)+1
            curr=curr.next
        own=ListNode(0)
        new=own
        curr=head
        while curr:
            if li[curr.val]==1:
                new.next=ListNode(curr.val)
                new=new.next
            curr=curr.next
        return own.next
