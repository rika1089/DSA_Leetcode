# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # # DFS 
        # def dfs(node) :
        #     # If the subtree is empty i.e. root is NULL, return depth as 0
        #     if not node :
        #         return 0
            
        #     # Initialize the depth of two subtrees.
        #     if not node.left and not node.right :
        #         return 1

        #     # If the left subtree is empty, return the depth of right subtree after adding 1 to it
        #     if not node.left :
        #         return 1 + dfs(node.right)

        #     # If right subtree is empty , return the depth of left subtree after adding 1 to it
        #     if not node.right :
        #         return 1 + dfs(node.left)

        #     return 1 + min(dfs(node.left),dfs(node.right))
        
        # return dfs(root)

        # BFS
        if root is None: return 0
        depth = 1
        q = [root]
        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.pop(0)
                if (cur.left is None) and (cur.right is None): return depth
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            
            depth += 1
        
        return depth
