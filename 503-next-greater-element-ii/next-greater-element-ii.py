class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        if n == 0 : 
            return []
        res = [-1]*n
        stack = []
        
        # iterate twice over the array (to simulate circular array)
        for i in range(2*n) :
            cur = nums[i%n]
            # resolve indices whose next greater is curr
            while stack and cur > nums[stack[-1]] :
                idx = stack.pop()
                res[idx] = cur
            # push into stack 
            if i < n :
                stack.append(i)
        return res
