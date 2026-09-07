# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter_nodes = 0  # stores diameter measured in nodes

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            # path through node uses lh + rh + 1 nodes
            self.max_diameter_nodes = max(self.max_diameter_nodes, lh + rh + 1)
            return 1 + max(lh, rh)

        height(root)
        # convert to edges if needed: edges = nodes - 1 (and handle empty tree)
        return 0 if self.max_diameter_nodes == 0 else self.max_diameter_nodes - 1
