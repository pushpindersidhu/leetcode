from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.depth(root)
        return self.balanced

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        if abs(left_depth - right_depth) > 1:
            self.balanced = False

        return 1 + max(left_depth, right_depth)
