# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return False
        li=set()
        curr=head
        while curr:
            if curr in li:
                return True
            else:
                li.add(curr)
                curr=curr.next
        return False 
