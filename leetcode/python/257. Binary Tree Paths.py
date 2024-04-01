from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def backtrack(root: TreeNode, path: str):
            if not root.left and not root.right:
                res.append(path)
                return
            if root.left:
                backtrack(root.left, path + f"->{root.left.val}")
            if root.right:
                backtrack(root.right, path + f"->{root.right.val}")

        backtrack(root, str(root.val))
        return res
