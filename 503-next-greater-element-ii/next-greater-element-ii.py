class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        if n == 0 : 
            return []
        res = [-1]*n
        stack = []
        
        for i in range(2*n) :
            cur = nums[i%n]
            while stack and cur > nums[stack[-1]] :
                idx = stack.pop()
                res[idx] = cur
            
            if i < n :
                stack.append(i)
        return res
