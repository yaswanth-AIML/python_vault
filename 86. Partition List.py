# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less=[]
        great=[]
        curr=head
        while curr:
            if curr.val>=x:
                great.append(curr.val)
            else:
                less.append(curr.val)
            curr=curr.next
        curr=head
        li=less+great
        i=0
        while curr:
            curr.val=li[i]
            curr=curr.next
            i+=1
        return head
