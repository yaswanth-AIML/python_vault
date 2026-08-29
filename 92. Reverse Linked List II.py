# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        li=[]
        curr=head
        h=1
        while h<left:
            curr=curr.next
            h+=1
        k=h
        li=[]
        while k<=right:
            li.append(curr.val)
            k+=1
            curr=curr.next
        li.reverse()
        curr=head
        l=1
        id1=0
        while curr:
            if left<=l<=right:
                curr.val=li[id1]
                id1+=1
            l+=1
            curr=curr.next
        return head 
