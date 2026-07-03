class Solution:
    def firstoccur(self,nums : List[int],target : int) -> int :
        n = len(nums)
        low = 0
        high = n-1
        a1 = -1
        while low <= high : 
            mid = low + ( high - low ) // 2
            if nums[mid] == target :
                a1 =  mid
                high = mid - 1
            elif nums[mid] < target :
                low = mid + 1
            else :
                high = mid - 1

        return a1

    def lastoccur(self,nums : List[int],target : int) -> int :
        n = len(nums)
        low = 0
        high = n-1
        a2 = -1
        while low <= high : 
            mid = low + ( high - low ) // 2
            if nums[mid] == target :
                a2 =  mid
                low = mid + 1
            elif nums[mid] < target :
                low = mid + 1
            else :
                high = mid - 1
        return a2
         
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        ans[0] = self.firstoccur(nums,target)
        ans[-1] = self.lastoccur(nums,target)
        return ans
        
        