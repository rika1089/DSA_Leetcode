# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count_subtree = 0

        # IDEA :  just a Post - Order Traversal is enough
        # Left 
        # right
        # root   - perfrom cal here which we got from left , right nodes

        def dfs(node) :
            if not node :
                return (0,0)    # sum , count 
            
            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)
            
            total_sum = left_sum + right_sum + node.val
            total_cnt = left_cnt + right_cnt + 1  # 1 is for root node 

            if node.val == total_sum // total_cnt :  # Check whether Q'a is satisfied
                self.count_subtree += 1 
            
            return (total_sum, total_cnt)
        
        dfs(root)
        return self.count_subtree
            
            
            