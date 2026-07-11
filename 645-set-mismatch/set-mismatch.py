class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = {}
        n = len(nums)
        for num in nums :
            if num not in freq :
                freq[num] = 1
            else :
                freq[num] += 1
        
        for i in range(1,n+1) :
            if i not in freq :
                missing = i
            elif freq[i] == 2 :
                repeted = i
        
        return [repeted,missing]
        
