# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        # if len(root) == 1 :
        #     return [[root]]
        
        q = deque([root])
        traversal = list(list())
        while q : 
            lvl_size = len(q)
            lvl_vals = []
            for _ in range(len(q)) :
                node = q.popleft()
                lvl_vals.append(node.val)
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            traversal.append(lvl_vals)
        return traversal
            
