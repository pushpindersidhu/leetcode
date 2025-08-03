from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = deque([(0, root)])
        while queue:
            tmp = []
            while queue and queue[0][0] == len(res):
                depth, node = queue.popleft()
                tmp.append(node.val)

                if node.left:
                    queue.append((depth + 1, node.left))

                if node.right:
                    queue.append((depth + 1, node.right))

            res.append(tmp)

        return res
