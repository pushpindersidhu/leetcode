from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.recurse(root)

        return self.diameter

    def recurse(self, root):
        if not root:
            return 0

        left_diameter = self.recurse(root.left)
        right_diameter = self.recurse(root.right)

        self.diameter = max(self.diameter, left_diameter + right_diameter)

        return 1 + max(left_diameter, right_diameter)
