class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # ans = []
        # for i in range(min(nums),max(nums)) :
        #     if i not in nums :
        #         ans.append(i)
        # return ans
        nums.sort()
        ans = []
        j = 0
        for i in range(min(nums),max(nums)) :
            if nums[j] != i :
                ans.append(i)
            else :
                j+=1
        
        return ans
    
    
