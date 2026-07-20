class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSum = nums[0]
        maxSum = nums[0]

        currMaxsum = nums[0]
        currMinsum = nums[0]

        totalsum = nums[0]

        for i in range(1,len(nums)) :

            currMaxsum = max(currMaxsum + nums[i], nums[i])
            maxSum = max(maxSum, currMaxsum)

            currMinsum = min(currMinsum + nums[i], nums[i])
            minSum = min(minSum, currMinsum)

            totalsum += nums[i]


        circularsum = totalsum -  minSum

        if circularsum == 0 :
            return maxSum

        
        return max(maxSum, circularsum)