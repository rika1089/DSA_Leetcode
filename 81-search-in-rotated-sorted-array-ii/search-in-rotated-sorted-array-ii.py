class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # TC : O(n)
        # for i,val in enumerate(nums) :
        #     if val == target :
        #         return i

        # return -1
        
        # Terms : 
        # 1 . Fixed Length (limited search space)
        # 2 . sorted

        l,h = 0 ,len(nums)-1

        while l <= h :
            mid = l + (h-l)//2

            if nums[mid] == target :
                return True # mid
                
            if nums[l] == nums[mid] and nums[mid] == nums[h] :
                l += 1
                h -= 1
                continue

            if nums[l] <= nums[mid] :
                if nums[l] <= target and target <= nums[mid] :
                    h = mid - 1
                else :
                    l = mid + 1
            
            else : # if nums[mid] < nums[h] :
                if nums[mid] <= target and target <= nums[h] :
                    l = mid + 1
                else :
                    h = mid - 1

        return False #-1