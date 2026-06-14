class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cntMap = {}
        for num in nums : 
            if num not in cntMap :
                cntMap[num] = 1
            else :
                cntMap[num] += 1
        
        # for key,val in cntMap.items() :
        #     if val >= n//2 :
        #         return key

        return max(cntMap,key=cntMap.get)
        