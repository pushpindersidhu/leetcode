"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        nodes_dict = {}

        new_head = Node(head.val)
        nodes_dict[head] = new_head

        curr = head.next
        new_curr = new_head
        while curr:
            new_curr.next = Node(curr.val)
            new_curr = new_curr.next

            nodes_dict[curr] = new_curr
            curr = curr.next

        curr = head
        new_curr = new_head
        while curr:
            random = curr.random

            if random:
                new_curr.random = nodes_dict[curr.random]
            else:
                new_curr.random = None

            curr = curr.next
            new_curr = new_curr.next

        return new_head
