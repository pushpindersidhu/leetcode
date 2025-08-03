from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque([(0, root)])
        while queue:
            right = 0
            while queue and queue[0][0] == len(res):
                depth, node = queue.popleft()
                right = node.val

                if node.left:
                    queue.append((depth + 1, node.left))

                if node.right:
                    queue.append((depth + 1, node.right))

            res.append(right)

        return res
