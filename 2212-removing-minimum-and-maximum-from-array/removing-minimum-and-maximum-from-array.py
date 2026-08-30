class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        Len = len(nums)
        if Len == 1 :
            return 1
        
        if Len == 2 :
            return 2
        
        maxi = float('-inf')
        maxi_idx = -1

        mini = float('inf')
        mini_idx = -1

        for i in range(Len) :
            if nums[i] > maxi :
                maxi = nums[i]
                maxi_idx = i
            
            if nums[i] < mini :
                mini = nums[i]
                mini_idx = i
        
        # Scenario 1 
        # if both are removed from Front
        steps_front = max(maxi_idx,mini_idx) + 1

        # Scenario 2 
        # if both are removed from Back
        steps_back = Len - min(maxi_idx,mini_idx) 

        # Scenario 3 
        # if both are removed from start
        steps_mixed = min(maxi_idx,mini_idx) + (Len - max(maxi_idx,mini_idx)) + 1

        return min(steps_mixed,min(steps_front,steps_back))