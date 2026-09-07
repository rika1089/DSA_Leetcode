# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative approach

        # if not root :
        #     return 0
        # queue = deque([root])
        # depth = 0
        # while queue :
        #     depth += 1
        #     for _ in range(len(queue)) :
        #         curr = queue.popleft()
        #         if curr.left :
        #             queue.append(curr.left)
        #         if curr.right :
        #             queue.append(curr.right)
        # return depth

        # DFS
        def dfs(node) :
            if not node :
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left,right)
        
        return dfs(root)


        