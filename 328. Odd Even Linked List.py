# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l1, l2 = [], []
        curr = head
        ol = True
        while curr:
            if ol:
                l1.append(curr.val)
            else:
                l2.append(curr.val)
            curr = curr.next
            ol = not ol
        curr = head
        for val in l1 + l2:
            curr.val = val
            curr = curr.next
        return head
