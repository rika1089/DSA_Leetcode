class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0 
        cnt = 0
        mini = float('inf')
        Sum = 0
        for j in range(len(nums)) :
            Sum += nums[j]
            while Sum >= target :
                if j - i + 1 < mini :
                    mini = (j-i+1)
                Sum -= nums[i]
                i += 1


        return mini if mini != float('inf') else 0