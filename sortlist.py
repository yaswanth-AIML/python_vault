# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        l=[]
        while curr:
            l.append(curr.val)
            curr=curr.next
        curr=head
        l.sort()
        for i in l:
            curr.val=i
            curr=curr.next
        return head
