class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsum = [0]
        
        for num in nums :
        
            runningsum.append(num + runningsum[-1])

        return runningsum[1:len(nums)+1]