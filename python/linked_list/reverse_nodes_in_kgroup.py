from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        i, curr = 1, head
        while curr and i != k:
            curr = curr.next
            i += 1

        if i != k or not curr:
            return head

        next = curr.next
        curr.next = None
        new_head = self.reverseList(head)
        head.next = self.reverseKGroup(next, k)

        return new_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
