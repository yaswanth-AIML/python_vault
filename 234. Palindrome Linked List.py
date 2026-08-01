# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr=[]
        cur=head
        while cur!=None:
            curr.append(cur.val)
            cur=cur.next
        left=0
        right=len(curr)-1
        while left<right:
            if curr[left]==curr[right]:
                left+=1
                right-=1
            else:
                return False
        return True
