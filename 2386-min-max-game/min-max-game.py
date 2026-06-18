class Solution :
 def minMaxGame(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    else:
        newNums = []
        maxArrLen = len(nums) // 2
                    
        for i in range(0, maxArrLen):
            if (i % 2 == 0):
                newNums.append(min(nums[2 * i], nums[2 * i + 1]))
            else:
                newNums.append(max(nums[2 * i], nums[2 * i + 1]))

        return self.minMaxGame(newNums)